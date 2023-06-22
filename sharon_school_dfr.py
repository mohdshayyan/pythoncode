
#                                                                                       ---| PYTHON CODING |---
#                                                                                 ---|School Management System|---
#                                                                             ---|  Designed and Maintained By  |---
#                                                                       ---| SHAYYAN - Class XII SCI {2023-2024}|---

import pandas as pd
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user='root',
  password='root',
  database='school ')
print(mydb,"connected to server")
print("\n")
print("-" *100)
print("                                     Welcome to  School Management System")
print("-" * 100)

# Define the function to add a new student
def create_database():
        cursor = mydb.cursor()
        cursor.execute('create database school')
        cursor.execute('use school')
def create_students():
        cursor = mydb.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS students (Id VARCHAR(255),name VARCHAR(255), age VARCHAR(255), gender VARCHAR(255), room_no VARCHAR(255))')
def add_student():
        id=input("Enter ID of student")
        name = input("Enter student Name: ")
        age = input("Enter student's age: ")
        gender = input("Enter student gender: ")
        room_no = input("Enter student Class: ")
        cursor = mydb.cursor()
# Inserting Values
        sql = "INSERT INTO students (id,name, age, gender, room_no) VALUES (%s,%s, %s, %s, %s)"
        val = (id,name, age, gender, room_no)
        cursor.execute(sql, val)
        mydb.commit()
        print(cursor.rowcount, "record(s) inserted.")
'''def fetch_id():
        sql="select id from students"
        val=(id,)
        cursor = mydb.cursor()
        cursor.execute(sql,val)
        result_id = cursor.fetchall()
        lst_id=[]
        for row in result_id:
                lst_id.append(row)
                print(lst_id)
def fetch_name():
        sql="select name from students"
        val=(name,)
        cursor = mydb.cursor()
        cursor.execute(sql,val)
        result_name = cursor.fetchall()
        lst_name=[]
        for row in result:
                lst_name.append(row)
                print(result_name)
def fetch_age():
        sql="select age from students"
        val=(age,)
        cursor = mydb.cursor()
        cursor.execute(sql,val)
        result_age = cursor.fetchall()
          lst_age=[]
          for row in result_age:
                lst_age.append(row)
                print(lst_age)
def fetch_gender():
        sql="select gender from students"
        val=(gender,)
        cursor = mydb.cursor()
        cursor.execute(sql,val)
        result_gen = cursor.fetchall()
        lst_gender=[]
        for row in result:
            lst_gender.append(row)
            print(lst_gender)
def fetch_room():
        sql="select room_no from students"
        val=(room_no,)
        cursor.execute(sql,val)
        result = cursor.fetchall()
        lst_room=[]
        for row in result:
            lst_room.append(row)
            print(lst_room)'''
'''
# Define the function to view student details
def view_students():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM students")
    result = cursor.fetchall()
    for row in result:
        result_list = [list(row) for row in result]
    print(result_list)
    lst1=[result_list[0][0],result_list[1][0],result_list[2][0],result_list[3][0],result_list[4][0]]
    print("lst1 is:",lst1)
    lst2=[result_list[0][1],result_list[1][1],result_list[2][1],result_list[3][1],result_list[4][1]]
    print('lst 2 is:',lst2)
    lst3=[result_list[0][2],result_list[1][2],result_list[2][2],result_list[3][2],result_list[4][2]]
    print('lst 3',lst3)
    lst4=[result_list[0][3],result_list[1][3],result_list[2][3],result_list[3][3],result_list[4][3]]
    print('lst 4 is: ',lst4)
    lst5=[result_list[0][4],result_list[1][4],result_list[2][4],result_list[3][4],result_list[4][4]]
    print('list 5',lst5)
    df=pd.DataFrame({'ID':lst1,'Name':lst2,'Age':lst3,'Gender':lst4,'Room_No':lst5})
    print(df.to_markdown())
'''
# Define the function to view student details
def view_students():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM students")
    result = cursor.fetchall()
    result_list = [list(row) for row in result]
    print(result_list)
    lst1 = [row[0] for row in result_list]
    print("lst1 is:", lst1)
    lst2 = [row[1] for row in result_list]
    print('lst 2 is:', lst2)
    lst3 = [row[2] for row in result_list]
    print('lst 3', lst3)
    lst4 = [row[3] for row in result_list]
    print('lst 4 is: ', lst4)
    lst5 = [row[4] for row in result_list]
    print('list 5', lst5)
    df = pd.DataFrame({'ID': lst1, 'Name': lst2, 'Age': lst3, 'Gender': lst4, 'Room_No': lst5})
    print(df.to_markdown())    

                       
     
# Define the function to update student details
def update_student():
    id = input("Enter student's ID: ")
    name = input("Enter student's Name: ")
    age = input("Enter studenlt's age: ")
    gender = input("Enter student's gender: ")
    room_no = input("Enter student's Class: ")
    cursor = mydb.cursor()
    sql_up = "update students set name = %s, age = %s, gender = %s, room_no = %s where id = %s"
    val_up = (name, age, gender, room_no,id)
    cursor.execute(sql_up, val_up)
    mydb.commit()
    print(cursor.rowcount, "record(s) updated.")

# Define the function to delete student details
def delete_student():
    id = input("Enter student ID: ")
    cursor = mydb.cursor()
    sql = "delete from students where id = %s"
    val = (id,)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record(s) deleted.")

    # CREATING A TABLE
def create_Staff():
        cursor = mydb.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS Staff(Id varchar(50) primary key,post varchar(50),name varchar(50),salary varchar(50),phone varchar(50))')

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
    result_list = [list(row) for row in result]
    print(result_list)
    lst1 = [row[0] for row in result_list]
    print("lst1 is:", lst1)
    lst2 = [row[1] for row in result_list]
    print('lst 2 is:', lst2)
    lst3 = [row[2] for row in result_list]
    print('lst 3', lst3)
    lst4 = [row[3] for row in result_list]
    print('lst 4 is: ', lst4)
    lst5 = [row[4] for row in result_list]
    print('list 5', lst5)
    df=pd.DataFrame({'ID':lst1,'POST':lst2,'NAME':lst3,'SALARY':lst4,'PHONE':lst5})
    print(df.to_markdown())

        
# Define the function to update staff details
def update_staff():
    Id=input("Enter staff ID: ")
    post=input("Enter staff Post: ")
    name = input("Enter staff Name: ")
    salary = input("Enter staff Salary: ")
    phone = input("Enter staff Phone no: ")
    cursor = mydb.cursor()
    sql = "UPDATE staff set Id = %s , post= %s, name = %s, salary = %s, phone = %s WHERE Id = %s"
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
        cursor.execute('CREATE TABLE IF NOT EXISTS fee(SrNo varchar(50) primary key,Name varchar(50),Class varchar(50),Status varchar(50),Quarter varchar(50),PaidAmt varchar(50))')

# Define the function to add Fee details
def fee():
    SrNo = input("Enter Payer's ID: ")
    Name = input("Enter Payer's Name: ")
    Class = input("Enter Payer's Class: ")
    Status = input("Enter Status(Paid/Due) : ")
    Quarter = input("Enter Quarter : ")
    PaidAmt = input("Enter PaidAmt : ")
    cursor = mydb.cursor()
    
    # Inserting Values  
    msql = "INSERT INTO fee (SrNo, Name, Class, Status, Quarter, PaidAmt) VALUES (%s, %s, %s, %s, %s, %s)"
    valu = (SrNo, Name, Class, Status, Quarter, PaidAmt)
    cursor.execute(msql, valu)
    mydb.commit()
    print(cursor.rowcount, "record(s) inserted.")

# Define the function to view Fee details
def view_fee():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM fee")
    result = cursor.fetchall()
    result = cursor.fetchall()
    result_list = [list(row) for row in result]
    print(result_list)
    lst1 = [row[0] for row in result_list]
    print("lst1 is:", lst1)
    lst2 = [row[1] for row in result_list]
    print('lst 2 is:', lst2)
    lst3 = [row[2] for row in result_list]
    print('lst 3', lst3)
    lst4 = [row[3] for row in result_list]
    print('lst 4 is: ', lst4)
    lst5 = [row[4] for row in result_list]
    print('list 5', lst5)
    lst6 = [row[5] for row in result_list]
    print('list 6', lst6)    
    lst7 = [row[6] for row in result_list]
    print('lst 7 is: ',lst7)
    df=pd.DataFrame({'SrNo':lst1,'Name':lst2,'Class':lst3,'':lst4,'Status':lst5,'Quarter':lst6, 'PaidAmt':lst7})
    print(df.to_markdown())
# (SrNo,Name,Class,Status,Quarter,PaidAmt) 

# Define the function to update Fee details
def update_fee():
    SrNo = input("Enter student SrNo: ")
    Name = input("Enter student Name: ")
    Class = input("Enter student Class: ")
    Status = input("Enter student Status(Paid/Due): ")
    Quarter = input("Enter student Quarter: ")
    PaidAmt = input("Enter student PaidAmount: ")  
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
    print("_" * 100)
    print("----------------Modules in School Management System ---------")
    print("Module_1: Student record Module ")
    print("Module_2: Staff record Module")
    print("Module_3: Fee record Module")
    print("Module_4: Exit from the system")
    
    print("_" * 100) 
# Get the user's choice:
# if option first:
def getchoice():
    while True:
        menu()
        print("")
        ch = input("Enter your choice: ")
        if ch=='1':
            print("PRESS a: To Add New Student record                                       PRESS b: View Student details ")
            print("PRESS c: To Update Student details                                           PRESS d: Delete Student details")
            ch = input("Enter your choice: ")
            create_students()
            if ch=='a':
                add_student()
            elif ch=='b':
                view_students()
            elif ch=='c':
                update_student()
            elif ch=='d':
                delete_student()
## if option Second:
        elif ch=='2':
            print("PRESS e : Add New Staff record                                       PRESS f : View Staff details | ")
            print("PRESS g : Delete Staff details                                             PRESS h : UPDATE Staff details  ")
            opp =input("Enter your choice: ")
            create_Staff()
            if opp=='e':
                add_staff()
            elif opp=='f':
                view_staff()
            elif opp=='g':
                update_staff()
            elif opp=='h':
                delete_staff()
### if option Third:
        elif ch=='3':
            print("PRESS i: Add Fee deposit details                                        PRESS j: View Fee details ")
            print("PRESS k: Update Fee details                                                PRESS l: Delete Fee details")
            opp = input("Enter your choice: ")
            create_fee()
            if opp=='i':
                fee()
            elif opp=='j':
                view_fee()
            elif opp=='k':
                update_fee()
            elif opp=='l':
                delete_fee()
        
#### if option Fourth:
        elif ch=='4':
            print('Exit!!')
            break
        
# Recall Choice function =>
getchoice()
# Disconnecting from the server =>
mydb.close()

