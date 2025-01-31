import yaml
from datetime import datetime

class Note:
    def __init__(self, titre: str, contenu: str, categorie: str, tags: list, auteur: str = "Inconnu"): #le constructeur
        self.titre = titre #titre de la note
        self.contenu = contenu #contenu de la note
        self.categorie = categorie #categorie de la note
        self.tags = tags #tags de la note
        self.auteur = auteur #auteur de la note
        self.date_creation = datetime.now().strftime("%Y-%m-%d") #date de création de la note (initité mtn)
        self.date_modification = self.date_creation #la date de la derniere modification de la note (initité mtn)



    def to_yaml(self) -> str:  #convertit la note en format texte avec un en-tête YAML.
        metadata = {
            "titre": self.titre,
            "date_creation": self.date_creation,
            "date_modification": self.date_modification,
            "categorie": self.categorie,
            "tags": self.tags,
            "auteur": self.auteur
        }
        yaml_header = yaml.dump(metadata, default_flow_style=False, allow_unicode=True) #Convertit metadata en texte YAML.
        return f"---\n{yaml_header}---\n\n{self.contenu}" #Retourne la note complète en texte

    def get_filename(self) -> str: #Génère le nom du fichier correspondant à la note
        return f"{self.titre.replace(' ', '_').lower()}.txt"