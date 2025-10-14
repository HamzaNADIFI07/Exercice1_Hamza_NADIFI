import json, os
from models.task import Task

DATA_FILE = "data/tasks.json"

class ToDoController:
    def __init__(self, view):
        self.view = view
        self.tasks = self._load()

    def _load(self):
        if not os.path.exists(DATA_FILE):
            return []
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [Task.from_dict(t) for t in data]

    def _save(self):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump([t.to_dict() for t in self.tasks], f, indent=2)

    def add_task(self, title):
        self.tasks.append(Task(title))
        self._save()
        self.view.show_message(f"✅ Tâche ajoutée : {title}")

    def display(self):
        self.view.show_tasks(self.tasks)


    def delete_task(self, index):
        try:
            removed = self.tasks.pop(index - 1)
            self._save()
            self.view.show_message(f"🗑️ Tâche supprimée : {removed.title}")
        except IndexError:
            self.view.show_message("❌ Numéro de tâche invalide.")
