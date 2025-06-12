import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "daksh2",
    password = "Daksh@123",
    port = "3306",
    database = "box"
)

mycursor = conn.cursor()
#mycursor.execute("CREATE TABLE todo(uniqueID INT PRIMARY KEY AUTO_INCREMENT, taskname VARCHAR(100), status VARCHAR(50)) AUTO_INCREMENT = 100")

def addtasks():
    task_name = input("enter task name")
    insert = "INSERT INTO todo(taskname) values(%s)"
    mycursor.execute(insert,(task_name,))
    conn.commit()
    print("task added")

def showlist():
    mycursor.execute("select ROW_NUMBER() over (ORDER BY uniqueID) as rownum, taskname, uniqueID, status FROM todo;")
    result = mycursor.fetchall()
    for x in result:
        print(x)

def deltasks():
    taskno = int(input("enter task's uniqueid you want to delete"))
    delete = "DELETE FROM todo WHERE uniqueID = %s"
    mycursor.execute(delete,(taskno,))
    conn.commit()
    print("task has been deleted")


while True:

    print("press 1 to Add tasks\n") 
    print("press 2 to show tasks\n")
    print("press 3 to remove tasks\n")
    x= input("choose any one option in the todo list\n")

    if x == "1":
        addtasks()

    elif x == "2":
        showtask()

    elif x == "3":
        deltasks()