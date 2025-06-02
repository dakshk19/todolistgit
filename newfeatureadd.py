import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "daksh2",
    password = "Daksh@123",
    port = "3306",
    database = "box"
)

mycursor = conn.cursor()
#mycursor.execute("CREATE TABLE list(tasknumber VARCHAR(20), taskname VARCHAR(100))")

def addtasks():
    taskno = input("enter task number")
    task_name = input("enter task name")
    insert = "INSERT INTO list(tasknumber,taskname) values(%s,%s)"
    values = (taskno,task_name)
    mycursor.execute(insert,values)
    conn.commit()
    print("task added")


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