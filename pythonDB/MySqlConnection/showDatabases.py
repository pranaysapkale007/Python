import mysql.connector

myconn = mysql.connector.connect(host="localhost", user="root", passwd="admin", port='3306')

cur = myconn.cursor()

try:
    dbs = cur.execute("show databases")
except:
    myconn.rollback()


for x in cur:
    print(x)
myconn.close()
