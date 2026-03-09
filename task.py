class Task:
    def __init__(self, task_id, title, priority, completed=False):
        self.id = task_id
        self.title = title
        self.priority = priority
        self.completed = completed

    def mark_complete(self):
        self.completed = True
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "priority": self.priority,
            "completed": self.completed
        }
    
    def __str__(self):
        status = "✓" if self.completed else "x"
        return f"[{status}] {self.id}: {self.title} [{self.priority}]"