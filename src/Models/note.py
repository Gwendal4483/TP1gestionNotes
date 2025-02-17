import yaml
from datetime import datetime
import re

class Note:
    def __init__(self, titre: str, contenu: str, categorie: str, tags: list, auteur: str = "Inconnu",
                 date_creation: str = None, date_modification: str = None): 
        self.titre = titre
        self.contenu = contenu
        self.categorie = categorie
        self.tags = tags
        self.auteur = auteur
        self.date_creation = date_creation if date_creation else datetime.now().strftime("%Y-%m-%d")
        self.date_modification = date_modification if date_modification else self.date_creation

    def to_yaml(self) -> str:
        metadata = {
            "titre": self.titre,
            "date_creation": self.date_creation,
            "date_modification": self.date_modification,
            "categorie": self.categorie,
            "tags": self.tags,
            "auteur": self.auteur
        }
        yaml_header = yaml.dump(metadata, default_flow_style=False, allow_unicode=True)
        return f"---\n{yaml_header}---\n\n{self.contenu}"

    

    def get_filename(self) -> str:
        """Génère un nom de fichier sécurisé basé sur le titre en retirant les caracteres spéciaux."""
        safe_title = "".join(c if c.isalnum() or c in (" ", "-") else "" for c in self.titre)  # Supprime caractères spéciaux
        safe_title = "_".join(safe_title.strip().split())  # Remplace espaces par des "_"
        return f"{safe_title.lower()}.txt"

    @staticmethod
    def from_yaml(yaml_text: str) -> "Note":
        """Recrée une Note à partir d'un texte YAML"""
        parts = yaml_text.split("---\n")  # Séparer le YAML du contenu
        if len(parts) < 3:
            raise ValueError("Format YAML invalide")

        metadata_yaml = parts[1]
        contenu = parts[2].strip()

        metadata = yaml.safe_load(metadata_yaml)

        return Note(
            titre=metadata.get("titre", "Sans titre"),
            contenu=contenu,
            categorie=metadata.get("categorie", "Non classé"),
            tags=metadata.get("tags", []),
            auteur=metadata.get("auteur", "Inconnu"),
            date_creation=metadata.get("date_creation"),
            date_modification=metadata.get("date_modification")
        )
