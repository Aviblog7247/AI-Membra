import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", port ="3306", password="Praveen*1234",database="new_emp")

mycursor = mydb.cursor()
mycursor.execute('')
user= mycursor.fetchone()

import numpy
speed=[10,20,30,35,40,45,60,65]
x= numpy.mean(speed)
print(x)