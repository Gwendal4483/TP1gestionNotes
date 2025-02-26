
---

```md
# 📝 TP1 Gestion de Notes


### 📌 **Gestion des Notes**
- Ajouter une nouvelle note  
- Modifier une note existante  
- Supprimer une note  
- Afficher la liste des notes  
- Afficher le contenu d'une note  

### 📂 **Gestion des Catégories**
- **Lister** les catégories existantes  
- **Créer** une nouvelle catégorie  
- **Renommer** une catégorie  
- **Supprimer** une catégorie  

### 🔍 **Recherche et Affichage**
- Rechercher une note par **titre** ou **catégorie**  
- Afficher les notes d'une **catégorie spécifique**  

### 💾 **Sauvegarde et Chargement**
- **Sauvegarde automatique** des notes sous forme de fichiers  
- **Organisation des notes** dans des dossiers correspondant aux catégories  
- **Chargement automatique** des notes au démarrage  

---

## 📁 Structure du Projet

```
TP1gestionNotes/
│── notes/                  # Dossier contenant les notes (classées par catégories)
│   ├── Travail/            # Exemple de catégorie
│   ├── Personnel/          # Exemple de catégorie
│   ├── Autres/             # Autres notes
│── src/                     # Code source
│   ├── models/              # Modèles de données (Note)
│   ├── services/            # Gestionnaire de notes et catégories
│   ├── utils/               # Utilitaires (gestion de fichiers)
│   ├── main.py              # Programme principal
│── README.md                # Documentation
│── requirements.txt         # Dépendances (si nécessaire)
```

---

## 🎯 Installation et Exécution

### 1️⃣ Cloner le projet
```bash
git clone https://github.com/Gwendal4483/TP1gestionNotes.git
cd TP1gestionNotes
```

### 2️⃣ Installer les dépendances (si besoin)
Si le projet utilise des bibliothèques externes (comme `PyYAML`), installe-les :
```bash
pip install -r requirements.txt
```

### 3️⃣ Lancer l'application
```bash
python -m src.main
```

---

## 🛠 Utilisation


```
=== Gestionnaire de Notes ===
1. Gérer les notes
2. Gérer les catégories
3. Rechercher
4. Gérer les sauvegardes
5. Quitter
Votre choix (1-5) :
```

---

### 📌 **1. Gestion des Notes**
```
=== Gestion des Notes ===
1. Créer une nouvelle note
2. Modifier une note
3. Supprimer une note
4. Afficher une note
5. Retour au menu principal
```
- Lors de la création d’une note, il est possible de **choisir une catégorie existante** ou **en créer une nouvelle**.  
- Chaque note est enregistrée dans un **fichier texte au format YAML** dans le dossier de sa catégorie.

---

### 📂 **2. Gestion des Catégories**
```
=== Gestion des Catégories ===
1. Lister les catégories
2. Ajouter une catégorie
3. Renommer une catégorie
4. Supprimer une catégorie
5. Retour au menu principal
```
- **Ajout d’une catégorie** : Création d’un **nouveau dossier** pour organiser les notes.  
- **Renommage d’une catégorie** : Déplace les notes vers un **nouveau dossier**.  
- **Suppression d’une catégorie** : Supprime le dossier et toutes ses notes (après confirmation).  

---

### 🔍 **3. Recherche et Affichage**
- **Rechercher une note** par titre ou par catégorie.  
- **Afficher toutes les notes** d’une catégorie spécifique.  
- **Consulter le contenu** d’une note.  

---

## 📝 Format de Sauvegarde des Notes

Les notes sont enregistrées sous forme de **fichiers texte** avec un en-tête **YAML** pour stocker les métadonnées :

```yaml
---
titre: "Ma première note"
date_creation: "2025-02-20"
date_modification: "2025-02-20"
categorie: "Travail"
tags: ["python", "projet"]
auteur: "Gwendal"
---
Voici le contenu de la note...
```

