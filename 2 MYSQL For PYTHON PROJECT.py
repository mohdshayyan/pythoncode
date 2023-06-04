
#                                                                                       ---| PYTHON CODING |---
#                                                                                 ---|School Management System|---
#                                                                             ---|  Designed and Maintained By  |---
#                                                                       ---| SHAYYAN - Class XII SCI {2023-2024}|---

import mysql.connector


# Connecting from the server

userName=input("\n ENTER MYSQL SERVER'S USERNAME: ")
print("*"*130)
password=input(" ENTER MYSQL SERVER'S PASSWORD: ")
print("*"*130)
mydb = mysql.connector.connect(
  host="localhost",
  user=userName,
  password=password,
  database="school")
print(mydb,"connected to server")
print("\n")
print("*"*140)
print("                                     ---| Welcome to  School Management System by Shayyan|---\n")
print("*" * 140)

# Define the function to add a new student
def create_students():
        cursor = mydb.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS students (Id VARCHAR(255),name VARCHAR(255), age VARCHAR(255), gender VARCHAR(255), room_no VARCHAR(255))')
def add_student():
        while True:
            Id=input("Enter Student SrNo: ")
            if serbyId(Id)> 0 :
                print("Duplicate Id, ENTER A VALID ID")        
            else:
                break
        name = input("Enter student Name: ")
        age = input("Enter student DOB: ")
        gender = input("Enter student gender: ")
        room_no = input("Enter student Class: ")
        cursor = mydb.cursor()

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

    # CREATING A TABLE
def create_Staff():
        cursor = mydb.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS Staff(Id varchar(50),post varchar(50),name varchar(50),salary varchar(50),phone varchar(50))')

# Define the function to add a new staff
def add_staff():
    Id=input("Enter staff ID: ")
    post=input("Enter staff Post: ")
    name = input("Enter staff Name: ")
    salary = input("Enter staff Salary: ")
    phone = input("Enter staff Phone no: ")
    cursor = mydb.cursor()


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

# CREATING A TABLE
def create_fee():
        cursor = mydb.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS fee(SrNo varchar(50),Name varchar(50),Class varchar(50),Status varchar(50),Quarter varchar(50),PaidAmt varchar(50))')

# Define the function to add Fee details
def fee():
    SrNo=input("Enter Payer SrNo: ")
    Name = input("Enter Payer Name: ")
    Class = input("Enter Payer Class: ")
    Status= input("Enter Status(Paid/Due) : ")
    Quarter= input("Enter Quarter : ")
    PaidAmt= input("Enter PaidAmt : ")
    cursor = mydb.cursor()

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

    # Execute the selected option
    # Get the user's choice
def menu():
    print("                                             --------------------------------------------------")    
    print("                                       ---| Modules in School Management System |---")
    print("                                             --------------------------------------------------")
    print("[1.]->| Student record Module |                                            [2.]->| Staff record Module |")
    print("[3.]->| Fee record Module |                                                   [4.]->| Exit |                        \n")

# Get the user's choice:
# if option first:
def getchoice():
    while True:
        menu()
        print("")
        option = input("Enter your choice: ")
        if option=='1':
            print("\n[0.]->| CREATE TABLE Student record | ")
            print("[1.]->| Add New Student record |                                           [2.]->|  View Student details | ")
            print("[3.]->| Update Student details |                                           [4.]->| Delete Student details | \n")
            opp = input("Enter your choice: ")
            if opp=='0':
                create_students()
                print("Table created successfully.")
            elif opp=='1':
                add_student()
                input("Press ENTER KEY to continue.....")
                print()
            elif opp=='2':
                view_students()
                input("Press ENTER KEY to continue.....")
                print()
            elif opp=='3':
                update_student()
                input("Press ENTER KEY to continue.....")
                print()
            elif opp=='4':
                delete_student()
                input("Press ENTER KEY to continue.....")
                print()

## if option Second:
        elif option=='2':
            print("\n[0.]->| Create Table Staff record | ")
            print("[1.]->| Add New Staff record |                                           [2.]->| View Staff details | ")
            print("[3.] ->| Update Staff details |                                          [4.]->| Delete Staff details | ")
            opp =input("Enter your choice: ")
            if opp=='0':
                create_Staff()
                print("Table created successfully.")
            elif opp=='1':
                add_staff()
                input("Press ENTER KEY to continue.....")
                print()
            elif opp=='2':
                view_staff()
                input("Press ENTER KEY to continue.....")
                print()
            elif opp=='3':
                update_staff()
                input("Press ENTER KEY to continue.....")
                print()
            elif opp=='4':
                delete_staff()
                input("Press ENTER KEY to continue.....")
                print()

### if option Third:
        elif option=='3':
            print("\n[0.]->| Create Table Fee record | ")
            print("[1.]->| Add Fee deposit details |                                            [2.]->| View Fee datails | ")
            print("[3.]->| Update Fee datails |                                                 [4.]->| Delete Fee datails | ")
            opp = input("Enter your choice: ")
            if opp=='0':
                create_fee()
                print("Table created successfully.")
            if opp=='1':
                fee()
                input("Press ENTER KEY to continue.....")
                print()
            elif opp=='2':
                view_fee()
                input("Press ENTER KEY to continue.....")
                print()
            elif opp=='3':
                update_fee()
                input("Press ENTER KEY to continue.....")
                print()
            elif opp=='4':
                delete_fee()
                input("Press ENTER KEY to continue.....")
                print()
#### if option Fourth:
        elif option=='4':
            print()
            print("Exited !")
            print("Succesfully,")
            print("Thanks")
            print("For")
            print("Coming :-)")
            print()
            print()
            print()
            print()
            break
        
# Recall Choice function =>
getchoice()
# Disconnecting from the server =>
mydb.close()

