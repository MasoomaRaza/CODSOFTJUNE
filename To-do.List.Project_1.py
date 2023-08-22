import time
import threading

class Task:
    def __init__(self, description, timer_minutes):
        self.description = description
        self.timer_minutes = timer_minutes
        self.completed = False
        self.start_time = None
        self.elapsed_time = 0

    def start(self):
        if not self.start_time:
            self.start_time = time.time()
            threading.Thread(target=self.update_timer).start()

    def stop(self):
        if self.start_time:
            self.elapsed_time += time.time() - self.start_time
            self.start_time = None

    def update_timer(self):
        while self.start_time:
            elapsed_time = time.time() - self.start_time
            if elapsed_time >= self.timer_minutes * 60:
                self.elapsed_time += elapsed_time
                self.start_time = None
            else:
                self.elapsed_time += elapsed_time
                time.sleep(1)

    def formatted_elapsed_time(self):
        minutes, seconds = divmod(int(self.elapsed_time), 60)
        return f"{minutes:02d}:{seconds:02d}"

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        task_list = []
        for index, task in enumerate(self.tasks, start=1):
            task_list.append(f"[{'✓' if task.completed else ' '}] {index}. {task.description} - {task.formatted_elapsed_time()} / {task.timer_minutes:02d}:00")
        return "\n".join(task_list)

    def mark_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1].completed = True

    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)

class TodoListApp:
    def __init__(self):
        self.todo_list = TodoList()

    def add_task(self, description, timer_minutes):
        new_task = Task(description, timer_minutes)
        self.todo_list.add_task(new_task)

    def view_tasks(self):
        return self.todo_list.view_tasks()

    def mark_completed(self, task_index):
        self.todo_list.mark_completed(task_index)

    def remove_task(self, task_index):
        self.todo_list.remove_task(task_index)

    def start_timer(self, task_index):
        self.todo_list.tasks[task_index - 1].start()

    def stop_timer(self, task_index):
        self.todo_list.tasks[task_index - 1].stop()

def main():
    app = TodoListApp()

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Remove Task")
        print("5. Start Timer")
        print("6. Stop Timer")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter the task: ")
            timer_minutes = int(input("Enter the timer duration in minutes: "))
            app.add_task(description, timer_minutes)
        elif choice == "2":
            print(app.view_tasks())
        elif choice == "3":
            task_index = int(input("Enter the task index to mark as completed: "))
            app.mark_completed(task_index)
        elif choice == "4":
            task_index = int(input("Enter the task index to remove: "))
            app.remove_task(task_index)
        elif choice == "5":
            task_index = int(input("Enter the task index to start the timer: "))
            app.start_timer(task_index)
        elif choice == "6":
            task_index = int(input("Enter the task index to stop the timer: "))
            app.stop_timer(task_index)
        elif choice == "7":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()