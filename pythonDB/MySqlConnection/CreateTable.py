import mysql.connector

myconn = mysql.connector.connect(host="localhost", user="root", passwd="admin", database="PythonDB2")

cur = myconn.cursor()

try:
    cur.execute("create table Employee ( name varchar(20), id int(20) not null primary key, salary float not null ) ")
except:
    myconn.rollback()


myconn.close()