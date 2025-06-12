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

def checkstatus():
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

def markdone():
    taskno = int(input("enter unique id of task which has to be mark done"))
    x = input("press 0 if task is pending \n press 1 if task is done")
    if x == "1":
        mark = "update todo set status = 'Done' where uniqueID=%s"
        mycursor.execute(mark,(taskno,))
        conn.commit()
        print("status marked as done")
    elif x == "0":
        mark = "update todo set status = 'pending' where uniqueID=%s"
        mycursor.execute(mark,(taskno,))
        conn.commit()
        print("status marked as pending")
    

while True:

    print("press 1 to Add tasks\n") 
    print("press 2 to Remove tasks\n")
    print("press 3 to Mark task done/pending \n")
    print("press 4 to Check status\n")
    x= input("choose any one option in the todo list\n")

    if x == "1":
        addtasks()

    elif x == "2":
        deltasks()

    elif x == "3":
        markdone()

    elif x == "4":
        checkstatus()