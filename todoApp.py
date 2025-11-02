Your_list = []
print("Welcome to your todo app!")
print("You can add, delete, and view your tasks.")
print("Let's get started!")

print("Your tasks are:", Your_list)
    # listeri gösterme

while True:
    # görev silme veya ekleme
     choose = input("do you want to add or delete a task? (add/delete/exit): ")
     choose = choose.lower()
     if choose == "add":
       print("You chose to add a task.")
       add_task = input("enter a task you want to add: ")
       Your_list.append(add_task)
       print("Task added. Your tasks are now:", Your_list)

     elif choose == "delete":
        print("You chose to delete a task.")
        delete_task = input("enter a task you want to delete: ")
        Your_list.remove(delete_task)
        print("Task deleted. Your tasks are now:", Your_list)
     elif choose == "exit":
        print("Exiting the todo app. Goodbye!")
        break
     else:
        print("Invalid choice. Please choose add, delete, or exit.")