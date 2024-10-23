import mysql.connector
from tabulate import tabulate

con = mysql.connector.connect(
	host="localhost",
	username="root",
	password="",
	database="test"
)

def insert(name, rollNo, gender, city):
	cur = con.cursor()
	query = "insert into student(name, roll_no, gender, city) values(%s, %s, %s, %s)"
	value = (name, rollNo, gender, city)
	cur.execute(query, value)
	con.commit()
	print("\n *** Data Insert Successful ***")

def update(rollNo, name, gender, city, sid):
	cur = con.cursor()
	query = "update student set name=%s, roll_no=%s, gender=%s, city=%s where id=%s"
	value = (name, rollNo, gender, city, sid)
	cur.execute(query, value)
	con.commit()
	print("\n *** Data Update Successful ***")

def selectAll():
	cur = con.cursor()
	query = "select id,name,roll_no,gender,city from student"
	cur.execute(query)
	result = cur.fetchall()
	print(tabulate(result, headers=["ID", "NAME", "ROLL NO.", "GENDER", "CITY"]))

def delete(sid):
	cur = con.cursor()
	query = "delete from student where id=%s"
	value = (sid,)
	cur.execute(query, value)
	con.commit()
	print("\n *** Delete Successful ***")


while True:
	print("\nStudent Management (CRUD) using Python & MySQL")
	print("**********************************************")
	print("\n1. Create (Insert)")
	print("2. Update")
	print("3. Read (Select)")
	print("4. Delete ")
	print("5. Exit")

	
	option = input("\nEnter Your Choice: ")
	
	if option == '1' or option.lower() == 'insert':
		#print("Insert Data")
		#print("-----------")
		rollNo = input("Enter Roll No.	: ")
		name = input("Enter Name 	: ")
		gender = input("Enter Gender	: ")
		city = input("Enter City	: ")
		insert(name, rollNo, gender, city)

	elif option == '2' or option.lower() == 'update':
		#print("Update Data")
		#print("-----------")
		rollNo = input("Enter Roll No.	: ")
		name = input("Enter Name 	: ")
		gender = input("Enter Gender	: ")
		city = input("Enter City	: ")
		sid = int(input("Enter Id	: "))
		update(rollNo, name, gender, city, sid)

	elif option == '3' or option.lower() == 'select':
		selectAll()		

	elif option == '4' or option.lower() == 'delete':
		sid = int(input("Enter Id	: "))
		delete(sid)

	elif option == '5' or option.lower() == 'exit':
		print("\n *** Thank You ***")
		break

	else:
		print("\n xx Invalid selection!, Please try again. xx")


