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

    @staticmethod
    def load_notes(folder: str = "data/"):
        notes = []
        if not os.path.exists(folder):
            return notes  # Retourne une liste vide si le dossier n'existe pas

        for filename in os.listdir(folder):
            filepath = os.path.join(folder, filename)

            with open(filepath, "r", encoding="utf-8") as file:
                yaml_content = file.read()
                note = Note.from_yaml(yaml_content)  # On suppose que Note a une méthode from_yaml()
                notes.append(note)

        print(f"{len(notes)} notes chargées depuis {folder}")
        return notes
