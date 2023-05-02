import mysql.connector
print("                                                 ---| Welcome to Cars Showroom by Mustufa---\n")
# Connecting from the server
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="car")
print(mydb,"connected to server")


# Define the function to add a new student
def add_Byuers_details():
    Car_Id=input("Enter the car Id: ")
    Name_of_ car = input("Enter the car name: ")
    car_Model = input("Enter the model name of the car: ")
    Name of Buyer = input("Enter the name of the buyer: ")
    Mode_payment= input("Enter the mode of payment: ")
    cursor = mydb.cursor()
    # CREATING A TABLE
   cursor.execute('CREATE TABLE Showrooms(Car_Id VARCHAR(255),Name_of_car VARCHAR(255),car_Model VARCHAR(255), Name of Buyer VARCHAR(255), Mode_payment VARCHAR(255))')

# Inserting Values
    sql = "INSERT INTO Showrooms (Car_Id,Name_of_ car , car_Model, Name of Buyer ,Mode_payment) VALUES (%s,%s, %s, %s, %s)"
    val = (Car_Id,Name_of_ car , car_Model, Name of Buyer ,Mode_payment)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record(s) inserted.")

# Define the function to view student details
def view_Showrooms():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Showrooms ")
    result = cursor.fetchall()
    for row in result:
        print(row)
        
# Define the function to update student details
def sales_record_Showrooms():
    Car_Id=input("Enter the car Id: ")
    Name_of_ car = input("Enter the car name: ")
    car_Model = input("Enter the Model name of the car: ")
    Name of Buyer = input("Enter the name of the buyer: ")
    Mode_payment= input("Enter the mode of payment: ")
    cursor = mydb.cursor()
    sql = "UPDATE Showrooms SET Name of Buyer = %s,Mode_payment = %s, Name_of_ car = %s,  car_Model= %s WHERE Car_Id = %s"
    val = ( Name of Buyer, Mode_payment, Name_of_ car, car_Model,Car_Id)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record(s) updated.")

# Define the function to delete student details
def delete_Showrooms_details():
      Car_Id=input("Enter the car Id: ")
    cursor = mydb.cursor()
    sql = "DELETE FROM students WHERE Car_Id = %s"
    val = (Car_Id,)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record(s) deleted.")


print("\n [1.] |add_Byuers_details |                                              [2.]  | view_Showrooms | ")
print("   [3.] | sales_record_Showrooms |                                              [4.]  |delete_Showrooms_details| \n")

opp = input("Enter your choice: ")
if opp=='1':
    add_student()
elif opp=='2':
    view_students()
elif opp=='3':
    update_student()
elif opp=='4':
    delete_student()

else:
    print("Invalid choice. Please try again.")

# Disconnecting from the server
mydb.close()
