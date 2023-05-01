import mysql.connector
# Connecting from the server
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="school")
print(mydb,"connected to server")

# Define the function to display the menu
def menu():
    print("                                                 ---| Welcome to System |---\n")
    print("(1.) Add New record                                          (2.) View details")
    print("(3.) Update details                                          (4.) Delete details")

# Define the function to add a new student
def addEmp():
    print("*******************ADD NEW EMPLOYEE**************************")
    eno =input("Enter employee number :")
    en = input("Enter employee name :")
    dp = input("Enter department ")
    sl = input("Enter Salary :")
    cursor = mydb.cursor()
    # CREATING A TABLE
    cursor.execute('CREATE TABLE  EMPLOYEE(enoVARCHAR(255),en VARCHAR(255),dp VARCHAR(255),sl VARCHAR(255))')
# Inserting Values
    sql = "INSERT INTO EMPLOYEE(eno,en, dp, sl) VALUES (%s, %s, %s, %s)"
    val = (eno,en, dp, sl)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record(s) inserted.")

# Call the menu function
while True:
    menu()
    
    # Get the user's choice
    choice = input("Enter your choice: ")

    # Execute the selected option
    if choice == '1':
        addEmp()
    else:
        print("Invalid choice. Please try again.")
# Disconnecting from the server
mydb.close()
