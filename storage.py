import json
from task import Task

class Storage:
    def __init__(self, filename = "tasks.json"):
        self.filename = filename

    def save_tasks(self, tasks):
        data = [task.to_dict() for task in tasks.values()]
        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)

    def load_tasks(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                tasks = {}
                for item in data:
                    task = Task(
                        item["id"],
                        item["title"],
                        item["priority"],
                        item["completed"],
                    )
                    tasks[item["id"]] = task
                return tasks
        except FileNotFoundError:
            return{}