from task import Task
from storage import Storage

class TaskManager:
    def __init__(self):
        self.storage = Storage()
        self.tasks = self.storage.load_tasks()
        self.next_id = max(self.tasks.keys(), default = 0) + 1

    def add_task(self, title):
        task = Task(self.next_id, title)
        self.tasks[self.next_id] = task
        self.next_id += 1
        return task
    def remove_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]           
            print("Task removed.")
        else:
            print("Task not found.")

    def mark_complete(self, task_id):
        if task_id in self.tasks:
            self.tasks[task_id].mark_complete()
            print("Task marked complete.")
        else:
            print("Task not found.")

    def get_all_tasks(self):
        return list(self.tasks.values())
    
    def save(self):
        self.storage.save_tasks(self.tasks)