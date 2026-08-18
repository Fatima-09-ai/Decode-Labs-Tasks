
my_tasks=[]
choice=""
print("Welcome to todo list app")
print("1- View your to-do list by pressing view\n2- Enter exit to exit this list\n3-Enter delete to remove the task from list\n4- Enter add to add task")
while choice!="exit":
    choice=input("Enter your choice:").lower()
    match choice:
      case "":
            print("Write something to add in a task😑")
      case "delete":
       if not my_tasks:
         print("Your task list is empty, nothing to delete.")
       else:
        print("Your tasks are...:-")
        for i,t in enumerate(my_tasks):
            print(f"{i+1}-",t["text"])
        try:
            index=int(input("Enter task number to delete:"))
            my_tasks.pop(index-1)
            print("Your tasks have been updated.")
        except (ValueError,IndexError):
            print("Thats not valid task number")
      case "view": 
            if not my_tasks:
                print("Your task list is empty")
            else:
             print("Your tasks are:-")
             for i,t in enumerate(my_tasks):
               status = "[x]" if t["done"] else "[ ]"
               print(f"{i+1}- {status} {t['text']}")
      case "exit":
          print("Exiting this program---")
      case "add":
        while True:
          task=input("Enter a task to add (or type 'done' to stop):")
          if task.lower()=="done":
            break
          elif task=="":
            print("Write something to add in a task😑")
          else:
            my_tasks.append({"text": task, "done": False})
            print(f'Added: "{task}"')
      case "complete":
         if not my_tasks:
          print("Your task list is empty.")
         else:
          print("Your tasks are...:-")
          for i,t in enumerate(my_tasks):
            status = "[x]" if t["done"] else "[ ]"
            print(f"{i+1}- {status} {t['text']}")
          try:
            index=int(input("Enter task number to mark complete:"))
            my_tasks[index-1]["done"] = True
            print("Congrats! You have completed the task...")
          except (ValueError,IndexError):
            print("That's not a valid task number.")  
      case _:
            print("Enter a valid task or command.")

print("Final tasks:")
for i,t in enumerate(my_tasks):
    print(f"{i+1}-",t["text"])
with open("tasks.txt","w") as f:
    for t in my_tasks:
        f.write(t["text"]+"\n")
