class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        return f"[{'x' if self.completed else ' '}] {self.description}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def update_task(self, index, description):
        if 0 <= index < len(self.tasks):
            self.tasks[index].description = description
        else:
            print("Task not found.")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_as_completed()
        else:
            print("Task not found.")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
            return
        for i, task in enumerate(self.tasks):
            print(f"{i + 1}. {task}")

def main():
    to_do_list = ToDoList()
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Complete Task")
        print("4. Display Tasks")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter task description: ")
            to_do_list.add_task(description)
        elif choice == '2':
            index = int(input("Enter task number to update: ")) - 1
            description = input("Enter new task description: ")
            to_do_list.update_task(index, description)
        elif choice == '3':
            index = int(input("Enter task number to mark as complete: ")) 
            to_do_list.complete_task(index)
        elif choice == '4':
            to_do_list.display_tasks()
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
