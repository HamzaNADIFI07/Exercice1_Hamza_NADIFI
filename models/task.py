from datetime import datetime

class Task:
    def __init__(self, title, done=False, created_at=None, id=None):
        self.id = id
        self.title = title
        self.created_at = created_at or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "created_at": self.created_at,
        }

    @staticmethod
    def from_dict(data):
        return Task(
            title=data["title"],
            created_at=data.get("created_at"),
            id=data.get("id"),
        )
