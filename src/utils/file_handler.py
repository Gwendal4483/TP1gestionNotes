import os
from src.models.note import Note

class FileHandler:
    @staticmethod
    def save_note(note: Note, folder: str = "data/"):
        if not os.path.exists(folder):
            os.makedirs(folder)

        filename = f"{folder}/{note.get_filename()}"

        with open(filename, "w", encoding="utf-8") as file:
            file.write(note.to_yaml())

        print(f"Note enregistrée dans {filename}")