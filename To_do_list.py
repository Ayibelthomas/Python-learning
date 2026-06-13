tasks = []
while True:
    print("To-Do List:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added.")
    elif choice == '2':
        if len(tasks) == 0:
            print("No tasks in the list.")
        else:
            print("Tasks:")
            for i in tasks:
                print("- " + i)
    elif choice == '3':
        task = input("Enter the task to remove: ")
        if task in tasks:
            tasks.remove(task)
            print("Task removed.")
        else:
            print("Task not found.")
    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
    