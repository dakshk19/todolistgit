tasks=[]


def addtasks():
    task = input("enter your task")
    tasks.append(task)
    print("task has been added")

def showtasks():
    idx=1
    for task in tasks:
        print(f"{idx}:{task}")
        idx+=1

def deltasks():

    if len(tasks) > 0:
        i = int(input("enter the task index that you want to delete"))
        tasks.pop(i-1)
        print("task has been removed ")

    else:
        print("list is empty so no item to delete")



while True:

    x= input("choose any one option in the todo list\n press 1 to add tasks \n press 2 to show tasks \n press 3 to remove tasks \n")

    if x == "1":
        addtasks()
    
    elif x == "2":
        showtasks()

    elif x == "3":
        deltasks()