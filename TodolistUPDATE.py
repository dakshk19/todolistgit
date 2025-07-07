import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "daksh2",
    password = "Daksh@123",
    port = "3306",
    database = "box"
)

mycursor = conn.cursor()

def addtasks(c_user):
    task_name = input("enter task name\n")
    insert = f"INSERT INTO {c_user}(taskname) values(%s)"
    mycursor.execute(insert,(task_name,))
    conn.commit()
    print("task added")
    runcmds(c_user)

def showlist(c_user):
    showlist = f"select ROW_NUMBER() over (ORDER BY uniqueID) as rownum, taskname, uniqueID,status FROM {c_user};"
    mycursor.execute(showlist)
    result = mycursor.fetchall()
    for x in result:
        print(x)
    runcmds(c_user)

def deltasks(c_user):
    taskno = int(input("enter task's uniqueid you want to delete"))
    delete = f"DELETE FROM {c_user} WHERE uniqueID = %s"
    mycursor.execute(delete,(taskno,))
    conn.commit()
    print("task has been deleted")
    runcmds(c_user)

def markdone(c_user):

    taskno = int(input("enter unique id of task which has to be mark done"))
    x = input("press 0 if task is pending \n press 1 if task is done")

    if x == "1":
        mark = f"update {c_user} set status = 'Done' where uniqueID= %s "

        mycursor.execute(mark,(taskno,))
        conn.commit()
        print("status marked as done")
        runcmds(c_user)

    elif x == "0":
        mark = f"update {c_user} set status = 'pending' where uniqueID=%s"
        mycursor.execute(mark,(taskno,))
        conn.commit()
        print("status marked as pending")
        runcmds(c_user)
    

def runcmds(c_user):

    while True:

        print("press 1 to Add tasks\n") 
        print("press 2 to Remove tasks\n")
        print("press 3 to Mark task done/pending \n")
        print("press 4 to See the TODOLIST\n")
        print("press 5 to go back\n")
        x= input("choose any one option in the todo list\n")

        if x == "1":
            addtasks(c_user)

        elif x == "2":
            deltasks(c_user)

        elif x == "3":
            markdone(c_user)

        elif x == "4":
            showlist(c_user)

        elif x == "5":
            break
        userfn()


def userfn():

    user = input("press 0 to go with existing user \npress 1 to create new user\n")

    if user == "1":

        newuser = input("enter name of new user\n")

        mycursor.execute("show tables")
        tables = mycursor.fetchall()
        if (newuser,) in tables:
            print("user is already present")

        else:
            table = f"CREATE TABLE IF NOT EXISTS {newuser}(uniqueID INT PRIMARY KEY AUTO_INCREMENT, taskname VARCHAR(100), status VARCHAR(50)) AUTO_INCREMENT = 100"
            mycursor.execute(table)
            conn.commit()
            print("new user has been created\n")

    if user == "0":

        c_user = input("enter name to the user you wanna go with\n")
        mycursor.execute("show tables")
        tables = mycursor.fetchall()

        if (c_user,) not in tables:
            print(f"no such user named {c_user}")

        else:
            runcmds(c_user)    

while True:
    

    userfn()

 




