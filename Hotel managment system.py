import mysql.connector
def menu():
    print("                                   --- Welcome to  Hotel Management System by Insha & Resham & Jiya ---\n")
    print("-" * 130)

# Connecting from the server

userName=input("\n ENTER MYSQL SERVER'S USERNAME: ")
print("-"*130)
password=input(" ENTER MYSQL SERVER'S PASSWORD: ")
print("-"*130)
mydb = mysql.connector.connect(
  host="localhost",
  user=userName,
  password=password,
  database="hotel")
print(mydb,"connected to server")
print("-"*130)

# Define the function to add a new guest
def add_guest():
        while True:
            print(" --- ENTER ROOM DETAILS  --- ")
            Id=input("Enter guest ID: ")
            name =input("Enter Guest Name : ") 
            rno = int(input("Enter Room No. : "))
            typ = input("Enter Room typ(Simple/Delux/Super Delux):")
            guest = int(input("Enter maximum number of guests : "))
            loc = input("Enter Location details : ")
            rent = int(input("Enter Per Day Charges : "))
            status =input("Vacant/Empty : ")
            cursor = mydb.cursor()
    # CREATING A TABLE
#            cursor.execute('CREATE TABLE Guests (Id VARCHAR(255),name VARCHAR(255),rno VARCHAR(255),typ VARCHAR(255), loc VARCHAR(255), guest VARCHAR(255),rent VARCHAR(255),status VARCHAR(255))')
# Inserting Values
            sql = "INSERT INTO Guests (Id,name,rno,typ,loc,guest,rent,status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (Id,name,rno,typ,loc,guest,rent,status)
            cursor.execute(sql, val)
            mydb.commit()
            print(cursor.rowcount, "record(s) inserted.")
            getchoice()
            
# Define the function to view Guest details
def view_Guests():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Guests")
    result = cursor.fetchall()
    for row in result:
        print(row)
        
        
# Define the function to update Guest details
def update_Guest():
    Id = input("Enter Guest Id: ")
    name =input("Enter Guest Name : ") 
    rno = int(input("Enter Room No. : "))
    typ = input("Enter Room typ(Simple/Delux/Super Delux):")
    guest = int(input("Enter maximum number of guests : "))
    loc = input("Enter Location details : ")
    rent = int(input("Enter Per Day Charges : "))
    status =input("Vacant/Empty : ")
    cursor = mydb.cursor()
    sql = "UPDATE Guests SET name = %s, rno = %s, typ = %s, guest = %s, loc = %s, rent= %s, status = %s WHERE Id = %s"
    val = (Id,name,rno,typ,loc,guest,rent,status)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record(s) updated.")    


# Define the function to delete Guest details
def delete_Guest():
    Id = input("Enter Guest Id: ")
    cursor = mydb.cursor()
    sql = "DELETE FROM Guests WHERE Id = %s"
    val = (Id,)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record(s) deleted.")
    
# Get the user's choice:
# if option first:
def getchoice():
    while True:
        menu()
        print("1. Create a New Room record                              2. Show All Rooms  ")
        print("3. Update Guest details                                       4. Delete Guest details  ")        
        print("5. Exit From The System\n")
        opp = input("Enter your choice: ")
        if opp=='1':
            add_guest()
            input("Press ENTER KEY to continue.....")
            print()
        elif opp=='2':
            view_Guests()                
            input("Press ENTER KEY to continue.....")
            print()
        elif opp=='3':
            update_Guest()
            input("Press ENTER KEY to continue.....")
            print()
        elif opp=='4':
            delete_Guest()
            input("Press ENTER KEY to continue.....")
            print()
        elif opp=='5':
            print('Exited !')
            break

# Recall Choice function =>
getchoice()
# Disconnecting from the server =>
mydb.close()
