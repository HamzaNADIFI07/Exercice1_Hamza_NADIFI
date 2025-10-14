import json
from datetime import datetime

class Task:
    def __init__(self, title, done=False, created_at=None):
        self.title = title
        self.done = done
        self.created_at = created_at or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {"title": self.title, "done": self.done, "created_at": self.created_at}

    @staticmethod
    def from_dict(data):
        return Task(data["title"], data["done"], data["created_at"])
