import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "daksh2",
    password = "Daksh@123",
    port = "3306",
    database = "box"
)

mycursor = conn.cursor()
#mycursor.execute("CREATE TABLE list (taskindex INT PRIMARY KEY AUTO_INCREMENT, taskname VARCHAR(100))")

def addtasks():
    task_name = input("enter task name")
    insert = "INSERT INTO list(taskname) values(%s)"
    mycursor.execute(insert,(task_name,))
    conn.commit()
    print("task added")


def showtasks():
    mycursor.execute("SELECT * FROM list")
    result = mycursor.fetchall()
    for x in result:
        print(x)


def deltasks():
    taskno = int(input("enter task number you want to delete"))
    delete = "DELETE FROM list WHERE taskindex = %s"
    mycursor.execute(delete,(taskno,))
    conn.commit()
    print("task has been deleted")
    
    

while True:

    x= input("choose any one option in the todo list\n press 1 to add tasks \n press 2 to show tasks \n press 3 to remove tasks \n")

    if x == "1":
        addtasks()
    
    elif x == "2":
        showtasks()

    elif x == "3":
        deltasks()