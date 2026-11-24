import requests

class NotesPage:
"""Page Object для взаимодействия с API заметок."""

def __init__(self, base_url="http://127.0.0.1:8000"):
    self.base_url = base_url
    self.notes_url = f"{base_url}/notes"

def get_all_notes(self):
    return requests.get(self.notes_url)

def create_note(self, payload):
    return requests.post(self.notes_url, json=payload)

def get_note(self, note_id):
    return requests.get(f"{self.notes_url}/{note_id}")

def update_note(self, note_id, payload):
    return requests.put(
        f"{self.notes_url}/{note_id}",
        json=payload
    )

def delete_note(self, note_id):
    return requests.delete(f"{self.notes_url}/{note_id}")