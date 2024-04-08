# Initialize an empty list to store to-do items
task_list = []

# Start an infinite loop to continually prompt the user for actions
while True:
    
    # Display Menu interface
    print("\n--------------------------------")
    print("          Task Manager          ")
    print("--------------------------------\n")
    print("[1] Add new Task")
    print("[2] Show all Tasks")
    print("[3] Edit a Task")
    print("[4] Complete a Task")
    print("[5] exit")

    # User Input
    user_action = input(">> ")
    # Remove any leading/trailing whitespace from the action
    user_action = user_action.strip()

    # Use pattern matching to handle the different user actions
    match user_action:
        case '1':  # Prompt for a new to-do item
            task = input("\nEnter a Task: ")
            # Append the new to-do item to the list
            task_list.append(task)
            print(f"\n[+] Task Added: {task}\n")
        case '2':  # Display all to-do items
            # If list is empty, show a message
            if task_list == []:
                print("\n[!] No Tasks to Display")
            else:
                print("\n--------------------------------")
                print("            Task List           ")
                print("--------------------------------")  

                # If list is not empty, display all tasks
                for index, task_item in enumerate(task_list):
                    # Enumerate through the list, displaying each item with a number
                    print(f"[{index+1}] {task_item}")
        case '3':  # Prompt for the item number to edit
            if not task_list:  # Checks if the task_list is empty
                print("\n[!] No tasks to edit.")
            else:
                task_number = int(input("\nTask List Number to Edit: "))
                # Ensure the task number is within the valid range
                if 1 <= task_number <= len(task_list):
                    new_task = input("Enter new task: ")
                    # Update the task in the list at the specified index
                    task_list[task_number - 1] = new_task
                else:
                    print("Invalid task number.")  # Inform the user if the task number is invalid
        case '4':  # If user types 'remove', prompt for the item number to remove
            if not task_list:
                print("\n[!] No tasks to Complete.")
            else:
                task_number = int(input("\nTask List Number to Complete: "))
                # Validate the task number and remove the task if valid
                if 1 <= task_number <= len(task_list):
                    # Remove the task from the list
                    completed_task = task_list.pop(task_number - 1)
                    print(f"[-] Task Completed: {completed_task}")
                else:
                    print("Invalid task number.")
        case '5':  # If user types 'exit', break the loop and end the program
            break
