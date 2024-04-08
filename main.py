todo_list = []

while True:
    print("\n--------------------------------")
    print("          Task Manager          ")
    print("--------------------------------\n")
    
    user_action = input("\nType add, show, edit, remove, or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("\nEnter a todo: ")
            todo_list.append(todo)
        case 'show':
            if todo_list == []:
                print("\n[-] No Tasks")
            else:
                print("\nToDo List:")
                for index, todo_item in enumerate(todo_list):
                    print(f"[{index+1}] {todo_item}")
        case 'edit':
            if not todo_list:  # Checks if the todo_list is empty
                print("\n[-] No tasks to edit.")
            else:
                task_number = int(input("\nTask List Number to Edit: "))
                if 1 <= task_number <= len(todo_list):  # Ensure task_number is within the valid range
                    new_todo = input("Enter new task: ")
                    todo_list[task_number - 1] = new_todo  # Corrected the list index to update the todo item
                else:
                    print("Invalid task number.")  # Notify user of invalid task number
        case 'remove':
            if not todo_list:
                print("\n[-] No tasks to remove.")
            else:
                task_number = int(input("\nTask List Number to Remove: "))
                if 1 <= task_number <= len(todo_list):
                    removed_task = todo_list.pop(task_number - 1)  # Remove the task and optionally store it if needed
                    print(f"Task removed: {removed_task}")
                else:
                    print("Invalid task number.")
        case 'exit':
            break