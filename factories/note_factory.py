import random
import string

class NoteFactory:

@staticmethod
def create_note(title=None, content=None):
    random_id = ''.join(
        random.choices(string.ascii_letters + string.digits, k=6)
    )

    return {
        "title": title or f"Тестовая заметка {random_id}",
        "content": content or f"Содержание заметки {random_id}"
    }

@staticmethod
def create_invalid_note():
    return {
        "title": "",
        "content": ""
    }