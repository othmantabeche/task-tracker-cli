from datetime import datetime


class Task:
    def __init__(self, id: int, description: str):
        self.id = id
        self.description = description
        self.status = "todo"
        self.createdAt = datetime.now().isoformat()
        self.updatedAt = self.createdAt

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt,
        }
