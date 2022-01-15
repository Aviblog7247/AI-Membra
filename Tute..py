import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", port ="3306", password="Praveen*1234",database="new_emp")

mycursor = mydb.cursor()
mycursor.execute('SELECT * FROM employee')
user= mycursor.fetchone()

for employee in user:
    print(user)
    print('Username'+ user[1])
    print('Password'+ user[2])