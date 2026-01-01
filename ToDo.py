tasks=[]
def show_menu():
  print("*** TO DO LIST ***")
  print("1.Add Task")
  print("2.view Task")
  print("3.Update Task")
  print("4.Delete Task")
  print("5.Exit")
while True:
  show_menu()
  choice=input("Enter your choice:\t")
  if choice=="1":
    task=input("enter task:\t")
    tasks.append(task)
    print("Task added ")
  elif choice=="2":
    if not tasks:
      print("No Tasks available.")
    else:
      for i , task in enumerate(tasks,start=1):
        print(f"{i}.{task}")
  elif choice =="3":
    if not tasks:
      print("No Task available.")
    else:
      for i,task in enumerate(tasks,start=1):
        print(f"{i}.{task}")
      num=int(input("enter task number to update:\t"))
      if 1<=num<=len(tasks):
        new_task=input("enter new task:\t")
        tasks[num-1]=new_task
        print("Task updated successfully!")
      else:
        print("Invalid task number.")
  elif choice=="4":
    num=int(input("Enter Task number to delete.\t"))
    if 1<=num<=len(tasks):
      tasks.pop(num-1)
      print("Task deleted!")
    else:
      print("Invalid task number.")
  elif choice == "5":
    print("Done for the day!")
    break
  else:
    print("Invalid choice.")

            
      
                        
  
  
