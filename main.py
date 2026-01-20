def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")

def show_menu():
    print("\nTask Manager")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Exit")


def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Choose: ")

        if choice == "1":
            task = input("Enter task: ")
            tasks.append(task)
            save_tasks(tasks)
            print("Task added.")
        elif choice == "2":
            if not tasks:
                print("No tasks.")
            else:
                for i, t in enumerate(tasks, 1):
                    print(f"{i}. {t}")
        elif choice == "3":
            break
        elif choice == "3":
            for i, t in enumerate(tasks, 1):
              print(f"{i}. {t}")
              num = int(input("Which task number? "))
              tasks[num-1] = tasks[num-1] + " [DONE]"
              save_tasks(tasks)
              print("Task marked as done.")

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
