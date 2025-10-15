from models.task import Task

class ToDoController:
    def __init__(self):
        self.next_id = 1
        self.tasks = []

    def list_tasks(self):
        """Retourne la liste de toutes les tâches"""
        return list(self.tasks)

    def _find_index_by_id(self, task_id: int):
        """Trouve la position d'une tâche via son ID"""
        for i, t in enumerate(self.tasks):
            if t.id == task_id:
                return i
        return -1

    def add_task(self, title: str):
        """Ajoute une nouvelle tâche"""
        title = (title or "").strip()
        if not title:
            raise ValueError("Le titre ne peut pas être vide.")
        new_task = Task(title=title, id=self.next_id)
        self.tasks.append(new_task)
        self.next_id += 1
        return new_task

    def get_task(self, task_id: int):
        """Récupère une tâche par son ID"""
        idx = self._find_index_by_id(task_id)
        if idx < 0:
            raise KeyError("Tâche introuvable.")
        return self.tasks[idx]

    def update_title(self, task_id: int, title: str):
        """Met à jour le titre d'une tâche"""
        title = (title or "").strip()
        if not title:
            raise ValueError("Le titre ne peut pas être vide.")
        idx = self._find_index_by_id(task_id)
        if idx < 0:
            raise KeyError("Tâche introuvable.")
        self.tasks[idx].title = title
        return self.tasks[idx]


    def delete_task(self, task_id: int):
        """Supprime une tâche par ID"""
        idx = self._find_index_by_id(task_id)
        if idx < 0:
            raise KeyError("Tâche introuvable.")
        removed = self.tasks.pop(idx)
        return removed.title
