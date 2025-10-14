import json, os
from models.task import Task

DATA_FILE = "data/tasks.json"

class ToDoController:
    def __init__(self):
        self.db = self._load_db()

    def _ensure_data_dir(self):
        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

    def _load_db(self):
        self._ensure_data_dir()
        if not os.path.exists(DATA_FILE):
            return {"next_id": 1, "tasks": []}

        with open(DATA_FILE, "r", encoding="utf-8") as f:
            raw = json.load(f)
        if isinstance(raw, list):
            tasks = []
            next_id = 1
            for t in raw:
                task = Task.from_dict(t)
                task.id = next_id
                tasks.append(task)
                next_id += 1
            return {"next_id": next_id, "tasks": tasks}

        tasks = [Task.from_dict(d) for d in raw.get("tasks", [])]
        next_id = raw.get("next_id", 1)
        changed = False
        for t in tasks:
            if t.id is None:
                t.id = next_id
                next_id += 1
                changed = True
        if changed:
            return {"next_id": next_id, "tasks": tasks}
        return {"next_id": next_id, "tasks": tasks}

    def _save_db(self):
        self._ensure_data_dir()
        payload = {
            "next_id": self.db["next_id"],
            "tasks": [t.to_dict() for t in self.db["tasks"]],
        }
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2)

    def list_tasks(self):
        return list(self.db["tasks"])

    def _find_index_by_id(self, task_id: int):
        for i, t in enumerate(self.db["tasks"]):
            if t.id == task_id:
                return i
        return -1

    def add_task(self, title: str):
        title = (title or "").strip()
        if not title:
            raise ValueError("Le titre ne peut pas être vide.")
        new = Task(title=title, id=self.db["next_id"])
        self.db["next_id"] += 1
        self.db["tasks"].append(new)
        self._save_db()
        return new

    def get_task(self, task_id: int):
        idx = self._find_index_by_id(task_id)
        if idx < 0:
            raise KeyError("Tâche introuvable.")
        return self.db["tasks"][idx]


    def update_title(self, task_id: int, title: str):
        title = (title or "").strip()
        if not title:
            raise ValueError("Le titre ne peut pas être vide.")
        idx = self._find_index_by_id(task_id)
        if idx < 0:
            raise KeyError("Tâche introuvable.")
        self.db["tasks"][idx].title = title
        self._save_db()
        return self.db["tasks"][idx]

    def delete_task(self, task_id: int):
        idx = self._find_index_by_id(task_id)
        if idx < 0:
            raise KeyError("Tâche introuvable.")
        removed = self.db["tasks"].pop(idx)
        self._save_db()
        return removed.title
