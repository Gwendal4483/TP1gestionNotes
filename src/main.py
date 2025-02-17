from services.note_manager import NoteManager


def main():
    manager = NoteManager()

    while True:
        print("\n=== Gestionnaire de Notes ===")
        print("1. Gérer les notes")
        print("2. Gérer les catégories")
        print("3. Rechercher")
        print("4. Gérer les sauvegardes")
        print("5. Quitter")

        choix = input("Votre choix (1-5) : ")

        if choix == "1":
            menu_gestion_notes(manager)
        elif choix == "2":
            print("Gestion des catégories (à implémenter)...")
        elif choix == "3":
            print("Recherche (à implémenter)...")
        elif choix == "4":
            print("Gestion des sauvegardes (à implémenter)...")
        elif choix == "5":
            print("Au revoir !")
            break
        else:
            print("Choix invalide, veuillez réessayer.")

def menu_gestion_notes(manager):
    """Sous-menu pour gérer les notes"""
    while True:
        print("\n=== Gestion des Notes ===")
        print("1. Créer une nouvelle note")
        print("2. Modifier une note")
        print("3. Supprimer une note")
        print("4. Afficher une note")
        print("5. Retour au menu principal")

        choix = input("Votre choix (1-5) : ")

        if choix == "1":
            titre = input("Titre : ")
            contenu = input("Contenu : ")
            categorie = input("Catégorie : ")
            tags = input("Tags (séparés par des virgules) : ").split(",")

            manager.ajouter_note(titre, contenu, categorie, tags)
        elif choix == "2":
            manager.modifier_note()
        elif choix == "3":
            manager.supprimer_note()
        elif choix == "4":
            manager.afficher_notes()
        elif choix == "5":
            break
        else:
            print("Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()