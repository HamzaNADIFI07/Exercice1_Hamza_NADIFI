# ToDoList

Une  application en ligne de commande (CLI) pour gérer ta liste de tâches directement depuis le terminal, en suivant l’architecture MVC (Model–View–Controller).
Aucune dépendance externe — tout repose sur la bibliothèque standard de Python.

---

##  Fonctionnalités

* Ajouter une nouvelle tâche
* Afficher la liste des tâches
* Marquer une tâche comme terminée
* Supprimer une tâche
* Sauvegarde automatique dans un fichier JSON

---
## Installation

1. **Télécharger** ou **cloner** le projet :

   ```bash
   git clone https://github.com/ton-utilisateur/Exercice1_Hamza_NADIFI.git
   cd Exercice1_Hamza_NADIFI
   ```
2. S'ssurer d’avoir **Python 3.8+** installé.
3. (Optionnel) Créer un **environnement virtuel** pour isoler le projet :

   ```bash
   python3 -m venv env
   source env/bin/activate  # (Windows : env\Scripts\activate)
   ```

---


## Utilisation

### Ajouter une tâche

```bash
python main.py add "Acheter du lait"
```

### Afficher la liste des tâches

```bash
python main.py list
```

Exemple :

```
[1] ❌ Acheter du lait (créée le 2025-10-14 14:32:00)
```

### Marquer une tâche comme terminée

```bash
python main.py done 1
```

Affiche :

```
✅ Tâche #1 marquée comme terminée.
```

### Supprimer une tâche

```bash
python main.py delete 1
```

Affiche :

```
🗑️ Tâche supprimée : Acheter du lait
```

---

## Fichier de sauvegarde

Les tâches sont automatiquement sauvegardées dans le fichier :

```
data/tasks.json
```

Ce fichier est créé automatiquement si nécessaire.

---

## Structure du projet

```
todolist_mvc/
├── main.py                     # Point d'entrée (Controller principal)
├── models/
│   └── task.py                 # Model : définit la classe Task
├── views/
│   └── cli_view.py             # View : gère l’affichage et les interactions utilisateur
├── controllers/
│   └── todo_controller.py      # Controller : relie la logique (model + view)
├── data/
│   └── tasks.json              # Fichier de sauvegarde
└── README.md
```

---

## Architecture MVC

Le projet respecte le modèle **MVC (Model–View–Controller)** :

| Couche         | Rôle                                  | Exemple                                           |
| -------------- | ------------------------------------- | ------------------------------------------------- |
| **Model**      | Gère les données et la logique métier | `Task`, gestion des attributs et de la sauvegarde |
| **View**       | Affiche les données à l’utilisateur   | `CLIView`, responsable des `print()`              |
| **Controller** | Fait le lien entre Model et View      | `ToDoController`, gère les commandes utilisateur  |

Cette séparation rend le code plus clair, maintenable et facile à faire évoluer.

---

## Exemple complet

```bash
python main.py add "Reviser mes cours"
python main.py add "Faire du sport"
python main.py list
python main.py done 1
python main.py list
python main.py delete 2
python main.py list
```

---