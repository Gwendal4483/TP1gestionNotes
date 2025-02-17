import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src.models.note import Note
from src.utils.file_handler import FileHandler

class NoteManager:
    def __init__(self):
        self.notes = FileHandler.load_notes()  # Charge les notes au démarrage

    def ajouter_note(self, titre, contenu, categorie, tags):
        note = Note(titre, contenu, categorie, tags)
        self.notes.append(note)
        FileHandler.save_note(note)
        print(f"Note '{titre}' ajoutée et sauvegardée.")

    def afficher_notes(self):
        if not self.notes:
            print("Aucune note disponible.")
            return

        # Affichage de la liste des notes
        print("Liste des notes :")
        for i, note in enumerate(self.notes):
            print(f"{i + 1}. {note.titre} ({note.categorie})")

        # Sélection de la note
        try:
            choix = int(input("\nEntrez le numéro de la note à afficher (0 pour annuler) : ")) - 1
            if choix == -1:
                print("Annulation de la sélection.")
                return
            if choix < 0 or choix >= len(self.notes):
                print("Numéro invalide, veuillez réessayer.")
                return

            note = self.notes[choix]

            # Affichage des détails de la note sélectionnée
            print("\n" + "=" * 30)
            print(f"Titre: {note.titre}")
            print(f"Auteur: {note.auteur}")
            print(f"Catégorie: {note.categorie}")
            print(f"Tags: {', '.join(note.tags)}")
            print(f"Date de création: {note.date_creation}")
            print(f"Date de modification: {note.date_modification}")
            print("Contenu:\n")
            print(note.contenu)
            print("=" * 30 + "\n")

        except ValueError:
            print("Veuillez entrer un nombre valide.")

