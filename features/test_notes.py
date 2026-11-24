import requests
import pytest
from pytest_bdd import scenarios, given, when, then, parsers

scenarios("steps/notes.feature")

BASE_URL = "http://127.0.0.1:8000"


@pytest.fixture
def state():
    return {}


@given("API заметок доступен")
def api_available(state):
    response = requests.get(f"{BASE_URL}/notes")
    assert response.status_code == 200


@when(parsers.parse(
    'я создаю заметку с заголовком "{title}" и содержанием "{content}"'
))
def create_note(state, title, content):
    response = requests.post(
        f"{BASE_URL}/notes",
        json={"title": title, "content": content}
    )
    state["response"] = response
    assert response.status_code == 200
    state["note_id"] = response.json()["id"]


@when("я запрашиваю список заметок")
def get_notes(state):
    state["response"] = requests.get(f"{BASE_URL}/notes")


@when("запрашиваю созданную заметку")
def get_created_note(state):
    note_id = state["note_id"]
    state["response"] = requests.get(
        f"{BASE_URL}/notes/{note_id}"
    )


@when("обновляю созданную заметку")
def update_created_note(state):
    note_id = state["note_id"]
    state["response"] = requests.put(
        f"{BASE_URL}/notes/{note_id}",
        json={
            "title": "Обновленная заметка",
            "content": "Новый текст"
        }
    )


@when("удаляю созданную заметку")
def delete_created_note(state):
    note_id = state["note_id"]
    state["response"] = requests.delete(
        f"{BASE_URL}/notes/{note_id}"
    )


@then("код ответа должен быть 200")
def check_status(state):
    assert state["response"].status_code == 200