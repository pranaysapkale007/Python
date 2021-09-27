import mysql.connector

myconn = mysql.connector.connect(host="localhost", user="root", passwd="admin", database="Pythondb2")

cur = myconn.cursor()

try:
    cur.execute("select * from Employee")
    result = cur.fetchall()

    for x in result:
        print(x)

except:
    myconn.rollback()

myconn.close()
