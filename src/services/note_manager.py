import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src.models.note import Note
from src.utils.file_handler import FileHandler

class NoteManager:
    def __init__(self):
        self.notes = []

    def ajouter_note(self, titre, contenu, categorie, tags):
        note = Note(titre, contenu, categorie, tags)
        self.notes.append(note)
        FileHandler.save_note(note)
        print(f"Note '{titre}' ajoutée et sauvegardée.")

    def afficher_notes(self):
        if not self.notes:
            print("Aucune note disponible.")
        for note in self.notes:
            print(note.titre, "-", note.categorie)