from datetime import datetime

class Task:
    def __init__(self, title, done=False, created_at=None, id=None):
        self.id = id
        self.title = title
        self.created_at = created_at or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

