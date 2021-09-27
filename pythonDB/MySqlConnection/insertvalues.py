import mysql.connector

myconn = mysql.connector.connect(host="localhost", user="root", passwd="admin", database="Pythondb2")

cur = myconn.cursor()

sql = "insert into Employee(name, id, salary) values(%s,%s,%s)"
val = [("John", 101, 25000),
       ("Pranay", 102, 35000),
       ("Raj", 103, 40000)]

try:
    cur.executemany(sql, val)
    myconn.commit()
except:
    myconn.rollback()

print("records inserted")
myconn.close()
