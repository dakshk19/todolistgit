import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "daksh2",
    password = "Daksh@123",
    port = "3306",
    database = "box"
)

mycursor = conn.cursor()

#mycursor.execute("create table person(name varchar(30), age int unsigned)")
#mycursor.execute("insert into person(name,age) values(%s,%s)",("daksh",20))

mycursor.execute("CREATE TABLE tasks(taskname VARCHAR(100))")