#                                                                                       ---| PYTHON CODING |---
#                                                                                 ---|School Management System|---
#                                                                             ---|  Designed and Maintained By  |---
#                                                                       ---| SHAYYAN - Class XII SCI {2023-2024}|---
import mysql.connector
userName=input("\n ENTER MYSQL SERVER'S USERNAME: ")
password=input("\n ENTER MYSQL SERVER'S PASSWORD: ")
# Connecting from the server
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="school")
print(mydb,"connected to server")

# Define the function to display the menu
def menu():
    print("*" * 130)
    print("                                                 ---| Welcome to  School Management System by Shayyan|---\n")
    print("*" * 130)
    #    print(". Exit")
    print("(1.) Add New Student record                                          (2.) View Student details")
    print("(3.) Update Student details                                            (4.) Delete Student details")
    print("(5.) Add new Staff record                                               (6.) View Staff details")    
    print("(7.) Update Staff details                                                 (8.) Delete Staff details")
    print("(9.) Add Fee deposit details                                           (10.) View Fee datails")
    print("(11.) Update Fee datails                                                  (12.) Delete Fee datails                     (13.) Exit")
# Define the function to add a new student
def add_student():
    Id=input("Enter Student SrNo: ")
    name = input("Enter student Name: ")
    age = input("Enter student DOB: ")
    gender = input("Enter student gender: ")
    room_no = input("Enter student Class: ")
    cursor = mydb.cursor()
    # CREATING A TABLE
#    cursor.execute('CREATE TABLE students (Id VARCHAR(255),name VARCHAR(255), age VARCHAR(255), gender VARCHAR(255), room_no VARCHAR(255))')
# Inserting Values
    sql = "INSERT INTO students (Id,name, age, gender, room_no) VALUES (%s,%s, %s, %s, %s)"
    val = (Id,name, age, gender, room_no)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record(s) inserted.")

# Define the function to view student details
def view_students():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM students")
    result = cursor.fetchall()
    for row in result:
        print(row)

# Define the function to update student details
def update_student():
    id = input("Enter student SrNo: ")
    name = input("Enter student Name: ")
    age = input("Enter student DOB: ")
    gender = input("Enter student gender: ")
    room_no = input("Enter student Class: ")
    cursor = mydb.cursor()
    sql = "UPDATE students SET name = %s, age = %s, gender = %s, room_no = %s WHERE id = %s"
    val = (name, age, gender, room_no, id)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record(s) updated.")

# Define the function to delete student details
def delete_student():
    Id = input("Enter student SrNo: ")
    cursor = mydb.cursor()
    sql = "DELETE FROM students WHERE Id = %s"
    val = (Id,)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record(s) deleted.")

# Define the function to add a new staff
def add_staff():
    Id=input("Enter staff ID: ")
    post=input("Enter staff Post: ")
    name = input("Enter staff Name: ")
    salary = input("Enter staff Salary: ")
    phone = input("Enter staff Phone no: ")
    cursor = mydb.cursor()

    # CREATING A TABLE
#    cursor.execute('create table Staff(Id varchar(50),post varchar(50),name varchar(50),salary varchar(50),phone varchar(50))')
# Inserting Values
    sqls = "INSERT INTO staff (Id,post,name,salary,phone) VALUES (%s,%s,%s, %s, %s)"
    vals = (Id,post,name,salary,phone)
    cursor.execute(sqls, vals)
    mydb.commit()
    print(cursor.rowcount, "record(s) inserted.")

# Define the function to view student details
def view_staff():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM staff")
    result = cursor.fetchall()
    for row in result:
        print(row)
        
# Define the function to update staff details
def update_staff():
    Id=input("Enter staff ID: ")
    post=input("Enter staff Post: ")
    name = input("Enter staff Name: ")
    salary = input("Enter staff Salary: ")
    phone = input("Enter staff Phone no: ")
    cursor = mydb.cursor()
    sql = "UPDATE staff SET post= %s, name = %s, salary = %s, phone = %s WHERE Id = %s"
    val = (Id,post,name,salary, phone)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record(s) updated.")

# Define the function to delete staff details
def delete_staff():
    Id = input("Enter staff ID: ")
    cursor = mydb.cursor()
    sql = "DELETE FROM staff WHERE Id = %s"
    val = (Id,)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record(s) deleted.")


# Define the function to add Fee details
def fee():
    SrNo=input("Enter Payer SrNo: ")
    Name = input("Enter Payer Name: ")
    Class = input("Enter Payer Class: ")
    Status= input("Enter Status(Paid/Due) : ")
    Quarter= input("Enter Quarter : ")
    PaidAmt= input("Enter PaidAmt : ")
    cursor = mydb.cursor()
# CREATING A TABLE
#    cursor.execute('create table fee(SrNo varchar(50),Name varchar(50),Class varchar(50),Status varchar(50),Quarter varchar(50),PaidAmt varchar(50))')
 # Inserting Values
    msql = "INSERT INTO fee (SrNo,Name,Class,Status,Quarter,PaidAmt) VALUES (%s,%s, %s, %s, %s,%s)"
    valu = (SrNo,Name,Class,Status,Quarter,PaidAmt)
    cursor.execute(msql, valu)
    mydb.commit()
    print(cursor.rowcount, "record(s) inserted.")

# Define the function to view Fee details
def view_fee():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM fee")
    result = cursor.fetchall()
    for row in result:
        print(row)
# Define the function to update Fee details
def update_fee():
    SrNo = input("Enter student SrNo: ")
    Name = input("Enter student Name: ")
    Class = input("Enter student Class: ")
    Status = input("Enter student Status(Paid/Due): ")
    Quarter = input("Enter student Quarter: ")
    PaidAmt = input("Enter student PaidAmt: ")  
    cursor = mydb.cursor()
    sqlx = "UPDATE fee SET Name = %s, Class = %s, Status = %s, Quarter = %s,PaidAmt = %s WHERE SrNo = %s"
    valx = (Name,Class,Status,Quarter,PaidAmt,SrNo)
    cursor.execute(sqlx, valx)
    mydb.commit()
    print(cursor.rowcount, "record(s) updated.")
    
# Define the function to delete Fee details
def delete_fee():
    SrNo = input("Enter student SrNo: ")
    cursor = mydb.cursor()
    sqle = "DELETE FROM fee WHERE SrNo = %s"
    vale = (SrNo,)
    cursor.execute(sqle, vale)
    mydb.commit()
    print(cursor.rowcount, "record(s) deleted.")

# Call the menu function
while True:
    menu()
    
    # Get the user's choice
    choice = input("Enter your choice: ")

    # Execute the selected option
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        update_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        add_staff()
    elif choice == '6':
        view_staff()
    elif choice == '7':
        update_staff()
    elif choice == '8':
        delete_staff()
    elif choice == '9':
        fee()
    elif choice == '10':
        view_fee()
    elif choice == '11':
        update_fee()
    elif choice == '12':
        delete_fee()
    elif choice == '13':
        print("Exited Succesfully, thanks for coming :-)")
        break
    else:
        print("Invalid choice. Please try again.")
# Disconnecting from the server
mydb.close()
