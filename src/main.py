def main():
    print("=== Gestionnaire de Notes ===")
    print("1. Créer une note")
    print("2. Voir les notes")
    print("3. Quitter")

    choix = input("Votre choix : ")
    if choix == "1":
            titre = input("Titre : ")
            contenu = input("Contenu : ")
            categorie = input("Catégorie : ")
            tags = input("Tags (séparés par des virgules) : ").split(",")

            manager.ajouter_note(titre, contenu, categorie, tags)


    elif choix == "2":
            manager.afficher_notes()
            
    elif choix == "3":
        print("Au revoir !")
        exit()
    else:
        print("Choix invalide.")

if __name__ == "__main__":
    main()