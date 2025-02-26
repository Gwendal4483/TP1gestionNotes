### **README.md**

---

## 📌 Fonctionnalités

✔ **Gestion des Notes**  
- Ajouter une note  
- Modifier une note  
- Supprimer une note  
- Afficher une note  

✔ **Gestion des Catégories**  
- Créer une catégorie  
- Renommer une catégorie  
- Supprimer une catégorie  


✔ **Sauvegarde et Organisation**  
- Enregistrement automatique des notes en fichiers YAML  
- Organisation des notes dans des **dossiers par catégorie**  
- Chargement automatique des notes au démarrage  

---

## 📂 Arborescence du Projet
```
TP1gestionNotes/
│── notes/                  # Dossier contenant les notes (classées par catégories)
│   ├── Travail/            # Exemple de catégorie
│   ├── Personnel/          # Exemple de catégorie
│   ├── Autres/             # Autres notes
│── src/                    # Code source
│   ├── models/             # Modèles de données (Note)
│   ├── services/           # Gestionnaire de notes et catégories
│   ├── utils/              # Utilitaires (gestion de fichiers)
│   ├── main.py             # Programme principal
│── README.md               # Documentation
│── requirements.txt        # Dépendances (si nécessaire)
```

---

## 🚀 Installation et Exécution

### 1️⃣ Cloner le projet  
```bash
git clone https://github.com/Gwendal4483/TP1gestionNotes.git
cd TP1gestionNotes
```

### 2️⃣ Installer les dépendances  
```bash
pip install -r requirements.txt
```

### 3️⃣ Lancer l'application  
```bash
python -m src.main
```

---

## 🎮 Utilisation

L’application fonctionne avec un **menu interactif** en ligne de commande :

```
=== Gestionnaire de Notes ===
1. Gérer les notes
2. Gérer les catégories
3. Rechercher une note
4. Quitter
Votre choix (1-4) :
```

### 📌 Gestion des Notes  
```
=== Gestion des Notes ===
1. Ajouter une nouvelle note
2. Modifier une note
3. Supprimer une note
4. Afficher une note
5. Retour au menu principal
```
- Lors de la création d'une note, l'utilisateur peut **choisir une catégorie existante** ou **en créer une nouvelle**.  
- Chaque note est enregistrée dans un fichier texte dans le dossier correspondant à sa catégorie.  

### 📂 Gestion des Catégories  
```
=== Gestion des Catégories ===
1. Lister les catégories
2. Ajouter une catégorie
3. Renommer une catégorie
4. Supprimer une catégorie
5. Retour au menu principal
```
- **Créer une catégorie** : Ajoute un **nouveau dossier** pour organiser les notes.  
- **Renommer une catégorie** : Déplace les notes existantes dans un **nouveau dossier**.  
- **Supprimer une catégorie** : Supprime le dossier et toutes ses notes (avec confirmation).  

### 🔍 Recherche et Affichage  
- Rechercher une note par **titre** ou **catégorie**  
- Afficher toutes les notes d'une **catégorie spécifique**  
- Consulter le **contenu détaillé** d’une note  

---

## 📄 Format des Notes

Les notes sont sauvegardées sous forme de fichiers **YAML**, organisées par **catégories** dans le dossier `notes/`.  

**Exemple d'une note :**  
```
notes/Travail/rapport_reunion.txt
```

**Contenu YAML :**  
```yaml
---
titre: "Rapport de réunion"
date_creation: "2025-02-20"
date_modification: "2025-02-20"
categorie: "Travail"
tags: ["réunion", "boulot"]
auteur: "Gwendal"
---
Compte-rendu de la réunion du 20 février 2025...
```
