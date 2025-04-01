import json

data = {
  "task1": "taskDesc"
}

def taskProgram():
    print("Hello! Welcome to the to do list application.")
    nameInput = input("Please Enter your name: ")

    taskInput = int(input("""
              ??????????????????
              Would you like to:
              1 - Display tasks
              2 - Add task
              3 - Remove Task
              4 - Complete Task
              ??????????????????
              """))
    while True:
      if taskInput == 1:
        print(f"{nameInput} Displaying Task")
        print("Task Displayed")
        break

      elif taskInput == 2:
        taskName = input("What is the task name? ")
        taskDesc = input("What is the task desc? ")
          
        print(f"{nameInput} Adding Task....")
        print(f"Task Added - \n{taskName} -- {taskDesc}")
        break
      
      elif taskInput == 3:
        print(f"{nameInput} Removing Task...")
        print("Task Removed")
        break

      elif taskInput == 4:
        taskInput = input("What task do you want to complete? ")
        print(f"{nameInput} Completed Task: {taskInput}.")
        break

      else:
        print("Try again:")
        taskProgram()

try:
  taskProgram()
  print("Task Program Successfully Runned.")
except ValueError:
  print("You need to enter a correct value in the inputs.")