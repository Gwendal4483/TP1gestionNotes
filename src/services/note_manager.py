import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src.models.note import Note
from src.utils.file_handler import FileHandler

class NoteManager:
    def __init__(self):
        self.notes = FileHandler.load_notes()  # Charge les notes au démarrage



    def ajouter_note(self, titre, contenu, tags):
        """Ajoute une note en choisissant une catégorie existante ou en créant une nouvelle."""
        categories = self.lister_categories()

        # Affichage des catégories existantes
        print("\nCatégories disponibles :")
        for i, cat in enumerate(categories, 1):
            print(f"{i}. {cat}")

        # Choix de la catégorie
        choix = input("\nEntrez le numéro de la catégorie ou tapez une nouvelle catégorie : ").strip()

        if choix.isdigit() and 1 <= int(choix) <= len(categories):
            categorie = categories[int(choix) - 1]
        else:
            categorie = choix.capitalize()  # Création d'une nouvelle catégorie

        # Correction : S'assurer que le chemin est bien "notes/<categorie>/"
        dossier_categorie = os.path.join("notes", categorie)

        # Création de la note
        note = Note(titre, contenu, categorie, tags)
        self.notes.append(note)

        FileHandler.save_note(note, dossier_categorie)  # Utilisation du chemin corrigé

        print(f"\nNote '{titre}' ajoutée dans la catégorie '{categorie}' et sauvegardée.")



    def lister_categories(self):
        """Retourne la liste des catégories disponibles (dossiers dans 'notes/')."""
        base_path = "notes/"
        if not os.path.exists(base_path):
            os.makedirs(base_path)
    
        return [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]

    def afficher_categories(self):
        """Affiche la liste des catégories disponibles"""
        categories = self.lister_categories()
        if categories:
            print("\nCatégories disponibles :")
            for i, cat in enumerate(categories, 1):
                print(f"{i}. {cat}")
        else:
            print("\nAucune catégorie disponible.")



    def ajouter_categorie(self):
        """Ajoute une nouvelle catégorie (dossier)"""
        categorie = input("Nom de la nouvelle catégorie : ").strip().capitalize()

        if not categorie:
            print("Nom de catégorie invalide.")
            return

        chemin = os.path.join("notes", categorie)
        if os.path.exists(chemin):
            print("Cette catégorie existe déjà.")
        else:
            os.makedirs(chemin)
            print(f"Catégorie '{categorie}' créée avec succès.")





    def supprimer_categorie(self):
        """Supprime une catégorie et toutes les notes à l'intérieur"""
        categories = self.lister_categories()

        if not categories:
            print("Aucune catégorie à supprimer.")
            return

        # Affichage des catégories
        print("\nCatégories disponibles :")
        for i, cat in enumerate(categories, 1):
            print(f"{i}. {cat}")

        # Sélection de la catégorie
        choix = input("\nEntrez le numéro de la catégorie à supprimer (0 pour annuler) : ").strip()
        if choix.isdigit() and 1 <= int(choix) <= len(categories):
            categorie = categories[int(choix) - 1]
        else:
            print("Annulation ou choix invalide.")
            return

        # Confirmation
        confirmation = input(f"Voulez-vous vraiment supprimer la catégorie '{categorie}' et toutes ses notes ? (y/n) : ").strip().lower()
        if confirmation != 'y':
            print("Suppression annulée.")
            return

        chemin = os.path.join("notes", categorie)
        try:
            import shutil
            shutil.rmtree(chemin)  # Supprime le dossier et tout son contenu
            print(f"Catégorie '{categorie}' supprimée avec succès.")
        except Exception as e:
            print(f"Erreur lors de la suppression : {e}")


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







    def renommer_categorie(self):
        """Renomme une catégorie (dossier)"""
        categories = self.lister_categories()

        if not categories:
            print("Aucune catégorie à renommer.")
            return

        # Affichage des catégories
        print("\nCatégories disponibles :")
        for i, cat in enumerate(categories, 1):
            print(f"{i}. {cat}")

        # Sélection de la catégorie à renommer
        choix = input("\nEntrez le numéro de la catégorie à renommer (0 pour annuler) : ").strip()
        if choix.isdigit() and 1 <= int(choix) <= len(categories):
            ancienne_categorie = categories[int(choix) - 1]
        else:
            print("Annulation ou choix invalide.")
            return

        # Demander le nouveau nom
        nouveau_nom = input(f"Entrez le nouveau nom pour '{ancienne_categorie}' : ").strip().capitalize()
        if not nouveau_nom or nouveau_nom in categories:
            print("Nom invalide ou déjà utilisé.")
            return

        # Renommage du dossier
        ancien_chemin = os.path.join("notes", ancienne_categorie)
        nouveau_chemin = os.path.join("notes", nouveau_nom)

        try:
            os.rename(ancien_chemin, nouveau_chemin)
            print(f"Catégorie renommée en '{nouveau_nom}'.")
        except Exception as e:
            print(f"Erreur lors du renommage : {e}")
    








    def modifier_note(self):
        """Affiche la liste des notes, permet d'en choisir une et de la modifier."""
        if not self.notes:
            print("Aucune note disponible à modifier.")
            return

        # Affichage de la liste des notes
        print("\nListe des notes disponibles :")
        for i, note in enumerate(self.notes):
            print(f"{i + 1}. {note.titre} ({note.categorie})")

        # Sélection d'une note
        try:
            choix = int(input("\nEntrez le numéro de la note à modifier (0 pour annuler) : ")) - 1
            if choix == -1:
                print("Annulation de la modification.")
                return
            if choix < 0 or choix >= len(self.notes):
                print("Numéro invalide, veuillez réessayer.")
                return

            note = self.notes[choix]

            # Affichage des infos actuelles
            print("\n=== Modification de la note ===")
            print(f"Titre actuel : {note.titre}")
            print(f"Catégorie actuelle : {note.categorie}")
            print(f"Tags actuels : {', '.join(note.tags)}")
            print("Contenu actuel :")
            print(note.contenu)

            # Modification des champs
            note.titre = input(f"Nouveau titre ({note.titre}) : ") or note.titre
            note.categorie = input(f"Nouvelle catégorie ({note.categorie}) : ") or note.categorie
            note.tags = input(f"Nouveaux tags (séparés par des virgules, {', '.join(note.tags)}) : ").split(",") or note.tags
            note.contenu = input("Nouveau contenu (laisser vide pour conserver l'ancien) : ") or note.contenu

            # Mise à jour de la date de modification
            from datetime import datetime
            note.date_modification = datetime.now().strftime("%Y-%m-%d")

            # Sauvegarde de la note modifiée
            FileHandler.save_note(note)
            print(f"\nNote '{note.titre}' modifiée avec succès !")

        except ValueError:
            print("Veuillez entrer un nombre valide.")





    def supprimer_note(self):
        """Affiche la liste des notes, permet d'en choisir une et de la supprimer avec confirmation."""
        if not self.notes:
            print("Aucune note disponible à supprimer.")
            return

        # Affichage de la liste des notes
        print("\nListe des notes disponibles :")
        for i, note in enumerate(self.notes):
            print(f"{i + 1}. {note.titre} ({note.categorie})")

        # Sélection d'une note
        try:
            choix = int(input("\nEntrez le numéro de la note à supprimer (0 pour annuler) : ")) - 1
            if choix == -1:
                print("Annulation de la suppression.")
                return
            if choix < 0 or choix >= len(self.notes):
                print("Numéro invalide, veuillez réessayer.")
                return

            note = self.notes[choix]

            # Confirmation avant suppression
            confirmation = input(f"Êtes-vous sûr de vouloir supprimer la note '{note.titre}' ? (y/n) : ").strip().lower()
            if confirmation != 'y':
                print("Suppression annulée.")
                return

            # Suppression de la note
            self.notes.pop(choix)

            # Suppression du fichier associé
            filename = f"data/{note.get_filename()}"
            if os.path.exists(filename):
                os.remove(filename)
                print(f"Fichier '{filename}' supprimé.")
            else:
                print("Aucun fichier associé trouvé.")

            print(f"\nNote '{note.titre}' supprimée avec succès !")

        except ValueError:
            print("Veuillez entrer un nombre valide.")
