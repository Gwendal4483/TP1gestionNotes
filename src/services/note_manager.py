import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src.models.note import Note
from src.utils.file_handler import FileHandler

class NoteManager:
    def __init__(self, notes_folder="notes/"):
        self.notes_folder = notes_folder
        self.notes = FileHandler.load_notes(self.notes_folder)  # Passer le dossier des notes


    def lister_notes(self, categorie):
        """Retourne la liste des notes dans une catégorie donnée."""
        dossier_categorie = os.path.join("notes", categorie)
        if not os.path.exists(dossier_categorie):
            return []
        return [f for f in os.listdir(dossier_categorie) if f.endswith(".txt")]


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


    def afficher_note(self):
        """Affiche le contenu d'une note."""
        categories = self.lister_categories()
        if not categories:
            print("Aucune catégorie disponible.")
            return

        # Choisir une catégorie
        print("\nCatégories disponibles :")
        for i, cat in enumerate(categories, 1):
            print(f"{i}. {cat}")

        choix_cat = input("\nChoisissez une catégorie : ").strip()
        if not choix_cat.isdigit() or not (1 <= int(choix_cat) <= len(categories)):
            print("Catégorie invalide.")
            return

        categorie = categories[int(choix_cat) - 1]
        notes = self.lister_notes(categorie)

        if not notes:
            print("Aucune note dans cette catégorie.")
            return

        # Choisir une note
        print("\nNotes disponibles :")
        for i, note in enumerate(notes, 1):
            print(f"{i}. {note}")

        choix_note = input("\nChoisissez une note à afficher : ").strip()
        if not choix_note.isdigit() or not (1 <= int(choix_note) <= len(notes)):
            print("Note invalide.")
            return

        fichier_selectionne = notes[int(choix_note) - 1]
        note_path = os.path.join("notes", categorie, fichier_selectionne)

        # Charger et afficher la note
        note = FileHandler.load_note(note_path)
        print("\n=== Détails de la Note ===")
        print(f"Titre       : {note.titre}")
        print(f"Catégorie   : {note.categorie}")
        print(f"Tags        : {', '.join(note.tags)}")
        print(f"Créée le    : {note.date_creation}")
        print(f"Dernière modif : {note.date_modification}")
        print("\nContenu :\n" + note.contenu)






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
        """Modifie une note existante."""
        categories = self.lister_categories()
        if not categories:
            print("Aucune catégorie disponible.")
            return

        # Choix de la catégorie
        print("\nCatégories disponibles :")
        for i, cat in enumerate(categories, 1):
            print(f"{i}. {cat}")

        choix_cat = input("\nChoisissez une catégorie : ").strip()
        if not choix_cat.isdigit() or not (1 <= int(choix_cat) <= len(categories)):
            print("Catégorie invalide.")
            return

        categorie = categories[int(choix_cat) - 1]
        notes = self.lister_notes(categorie)

        if not notes:
            print("Aucune note dans cette catégorie.")
            return

        # Choix de la note
        print("\nNotes disponibles :")
        for i, note in enumerate(notes, 1):
            print(f"{i}. {note}")

        choix_note = input("\nChoisissez une note à modifier : ").strip()
        if not choix_note.isdigit() or not (1 <= int(choix_note) <= len(notes)):
            print("Note invalide.")
            return

        fichier_selectionne = notes[int(choix_note) - 1]
        note_path = os.path.join("notes", categorie, fichier_selectionne)

        # Charger la note
        note = FileHandler.load_note(note_path)

        # Modifier la note
        print(f"\nModification de la note : {note.titre}")
        note.titre = input(f"Nouveau titre [{note.titre}] : ") or note.titre
        note.contenu = input(f"Contenu [{note.contenu[:30]}...] : ") or note.contenu
        note.tags = input(f"Tags [{', '.join(note.tags)}] : ").split(",") or note.tags

        # Sauvegarder les modifications
        os.remove(note_path)  # Supprimer l'ancien fichier
        FileHandler.save_note(note, os.path.join("notes", categorie))
        print("Note mise à jour avec succès.")




    def supprimer_note(self):
        """Supprime une note après confirmation."""
        categories = self.lister_categories()
        if not categories:
            print("Aucune catégorie disponible.")
            return

        # Choisir une catégorie
        print("\nCatégories disponibles :")
        for i, cat in enumerate(categories, 1):
            print(f"{i}. {cat}")

        choix_cat = input("\nChoisissez une catégorie : ").strip()
        if not choix_cat.isdigit() or not (1 <= int(choix_cat) <= len(categories)):
            print("Catégorie invalide.")
            return

        categorie = categories[int(choix_cat) - 1]
        notes = self.lister_notes(categorie)

        if not notes:
            print("Aucune note dans cette catégorie.")
            return

        # Choisir une note
        print("\nNotes disponibles :")
        for i, note in enumerate(notes, 1):
            print(f"{i}. {note}")

        choix_note = input("\nChoisissez une note à supprimer : ").strip()
        if not choix_note.isdigit() or not (1 <= int(choix_note) <= len(notes)):
            print("Note invalide.")
            return

        fichier_selectionne = notes[int(choix_note) - 1]
        note_path = os.path.join("notes", categorie, fichier_selectionne)

        confirmation = input(f"Voulez-vous vraiment supprimer '{fichier_selectionne}' ? (oui/non) : ").strip().lower()
        if confirmation == "oui":
            os.remove(note_path)
            print("Note supprimée avec succès.")
        else:
            print("Suppression annulée.")

