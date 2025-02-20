import os
import yaml
from src.models.note import Note

class FileHandler:
    @staticmethod
    def save_note(note: Note, folder: str = "notes/"):
        """Sauvegarde une note sous forme de fichier."""
        if not os.path.exists(folder):
            os.makedirs(folder)

        filename = os.path.join(folder, note.get_filename())

        with open(filename, "w", encoding="utf-8") as file:
            file.write(note.to_yaml())

        print(f"Note enregistrée dans {filename}")


    @staticmethod
    def load_notes(folder: str):
        """Charge toutes les notes d'une catégorie."""
        if not os.path.isdir(folder):  # Vérifier si c'est bien un dossier
            print(f"Erreur : {folder} n'est pas un dossier.")
            return []

        notes = []
        for filename in os.listdir(folder):
            if filename.endswith(".txt"):
                note_path = os.path.join(folder, filename)
                note = FileHandler.load_note(note_path)
                if note:
                    notes.append(note)

        return notes
    

    @staticmethod
    def load_note(filepath: str):
        """Charge une note spécifique."""
        if not os.path.exists(filepath):
            print(f"Erreur : Le fichier {filepath} n'existe pas.")
            return None

        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()

        # Extraction des métadonnées YAML
        if content.startswith("---"):
            parts = content.split("---", 2)
            if len(parts) >= 3:
                metadata_yaml = parts[1]
                contenu = parts[2].strip()
                metadata = yaml.safe_load(metadata_yaml)

                return Note(
                    titre=metadata.get("titre", "Sans titre"),
                    contenu=contenu,
                    categorie=metadata.get("categorie", "Sans catégorie"),
                    tags=metadata.get("tags", []),
                    auteur=metadata.get("auteur", "Inconnu"),
                )
        return None
