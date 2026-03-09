from task_manager import TaskManager

def show_menu():
    print("\n=== Task Manager ===")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task Complete")
    print("4. Remove Task")
    print("5. Exit")

def main():
    manager = TaskManager()

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            tasks = manager.get_all_tasks()
            if not tasks:
                print("No tasks found.")
            else:
                for task in tasks:
                    print(task)

        elif choice == "2":
            title = input("Enter task title: ")
            priority = input("Enter task priority (LOW/MED/HIGH): ")
            manager.add_task(title, priority)
            manager.save()
            print("Task added.")

        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to mark complete: "))
                manager.mark_complete(task_id)
                manager.save()
            except ValueError:
                print("Invalid ID.")
        
        elif choice == "4":
            try:
                task_id = int(input("Enter task ID to remove: "))
                manager.remove_task(task_id)
                manager.save()
            except ValueError:
                print("Invalid ID.")

        elif choice == "5":
            manager.save()
            print("Goodbye.")
            break
        
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()