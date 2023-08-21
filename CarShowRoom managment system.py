import mysql.connector

# Establishing the connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="car_showroom"
)
print(connection,"connected to server")

# Creating a cursor object to execute SQL queries
cursor = connection.cursor()

# Function to create the car showroom management system table
def create_table():
    query = """
    CREATE TABLE IF NOT EXISTS cars (
        id INT AUTO_INCREMENT PRIMARY KEY,
        brand VARCHAR(50),
        model VARCHAR(50),
        year INT,
        price DECIMAL(10, 2)
    )
    """
    cursor.execute(query)
    print("Table created successfully.")

# Function to insert a new car into the database
def insert_car():
    brand = input("Enter the brand: ")
    model = input("Enter the model: ")
    year = int(input("Enter the year: "))
    price = float(input("Enter the price: "))
    query = "INSERT INTO cars (brand, model, year, price) VALUES (%s, %s, %s, %s)"
    values = (brand, model, year, price)
    cursor.execute(query, values)
    connection.commit()
    print("Car inserted successfully.")

# Function to retrieve all cars from the database
def get_all_cars():
    query = "SELECT * FROM cars"
    cursor.execute(query)
    cars = cursor.fetchall()
    if len(cars) > 0:
        for car in cars:
            print(f"ID: {car[0]}, Brand: {car[1]}, Model: {car[2]}, Year: {car[3]}, Price: {car[4]}")
    else:
        print("No cars found.")

# Function to update the price of a car
def update_car_price():
    car_id = int(input("Enter the car ID: "))
    new_price = float(input("Enter the new price: "))
    query = "UPDATE cars SET price = %s WHERE id = %s"
    values = (new_price, car_id)
    cursor.execute(query, values)
    connection.commit()
    print("Car price updated successfully.")

# Function to delete a car from the database
def delete_car():
    car_id = int(input("Enter the car ID: "))
    query = "DELETE FROM cars WHERE id = %s"
    values = (car_id,)
    cursor.execute(query, values)
    connection.commit()
    print("Car deleted successfully.")
#################################################################
    
# Function to create both "cars" and "sales" tables
def Create_Sales():
    sale_id = input("Enter the sale id: ")
    car_id = input("Enter the car id: ")
    sale_date = input("Enter the sale date: ")
    sale_price = int(input("Enter the sale price: "))

    query_sales = """
    CREATE TABLE IF NOT EXISTS sales (
        sale_id INT AUTO_INCREMENT PRIMARY KEY,
        car_id INT,
        sale_date varchar(12),
        sale_price DECIMAL(10, 2)
    )
    """
    cursor.execute(query_sales)

    query = "INSERT INTO sales (sale_id, car_id, sale_date, sale_price) VALUES (%s, %s, %s, %s)"
    values = (sale_id, car_id, sale_date, sale_price)
    cursor.execute(query, values)
    connection.commit()
    print("Sale record inserted successfully.")

    
def view_sales():
    query = "SELECT * FROM sales"
    cursor.execute(query)
    sales = cursor.fetchall()
    if len(sales) > 0:
        for sale in sales:
            print(f"Sale ID: {sale[0]}, Car ID: {sale[1]}, Sale Date: {sale[2]}, Sale Price: {sale[3]}")
    else:
        print("No sales records found.")

def update_sale_price():
    sale_id = int(input("Enter the Sale ID: "))
    new_price = float(input("Enter the new sale price: "))
    query = "UPDATE sales SET sale_price = %s WHERE sale_id = %s"
    values = (new_price, sale_id)
    cursor.execute(query, values)
    connection.commit()
    print("Sale price updated successfully.")

def delete_sale():
    sale_id = int(input("Enter the Sale ID: "))
    query = "DELETE FROM sales WHERE sale_id = %s"
    values = (sale_id,)
    cursor.execute(query, values)
    connection.commit()
    print("Sale record deleted successfully.")
#################################################################
# Creating a cursor object to execute SQL queries
cursor = connection.cursor()

# Function to insert a new dealer into the database
def insert_dealer():
    name = input("Enter dealer's name: ")
    address = input("Enter dealer's address: ")
    contact = input("Enter dealer's contact number: ")
    query = """
    CREATE TABLE IF NOT EXISTS dealer (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50),
        address VARCHAR(100),
        contact VARCHAR(20)
    )
    """
    cursor.execute(query)    
    query = "INSERT INTO dealer (name, address, contact) VALUES (%s, %s, %s)"
    values = (name, address, contact)
    cursor.execute(query, values)
    connection.commit()
    print("Dealer inserted successfully.")

# Function to retrieve all dealers from the database
def View_Dealers():
    query = "SELECT * FROM dealer"
    cursor.execute(query)
    dealers = cursor.fetchall()
    if len(dealers) > 0:
        for dealer in dealers:
            print(f"ID: {dealer[0]}, Name: {dealer[1]}, Address: {dealer[2]}, Contact: {dealer[3]}")
    else:
        print("No dealers found.")

# Function to update dealer information
def update_Dealer():
    dealer_id = int(input("Enter the dealer ID: "))
    new_name = input("Enter the new name: ")
    new_address = input("Enter the new address: ")
    new_contact = input("Enter the new contact number: ")
    query = "UPDATE dealer SET name = %s, address = %s, contact = %s WHERE id = %s"
    values = (new_name, new_address, new_contact, dealer_id)
    cursor.execute(query, values)
    connection.commit()
    print("Dealer information updated successfully.")

# Function to delete a dealer from the database
def delete_dealer():
    dealer_id = int(input("Enter the dealer ID: "))
    query = "DELETE FROM dealer WHERE id = %s"
    values = (dealer_id,)
    cursor.execute(query, values)
    connection.commit()
    print("Dealer deleted successfully.")
#################################################################
# Menu loop
while True:
    print("\n                                                           \ CAR SHOWROOM MANAGEMENT SYSTEM /\n ")
    print("                                                           (1.) Create Table                              (2.) Insert Car")
    print("                                                           (3.) Get All Cars                              (4.) Update Car Price")
    print("                                                           (5.) Delete Car                                 (6.) Insert Sales")#(6.) Exit
    print("                                                           (7.)view sales                                   (8.)Update sale price ")
    print("                                                           (9.)delete sale                                  (10.)Insert Dealer")
    print("                                                           (11.)View Dealers                              (12.)Update Dealer ")
    print("                                                           (13.)Delete Dealer                             (14.)Exit \n   ")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        create_table()
    elif choice == "2":
        insert_car()
    elif choice == "3":
        get_all_cars()
    elif choice == "4":
        update_car_price()
    elif choice == "5":
        delete_car()
    elif choice == "6":
        Create_Sales()
    elif choice == "7":
        view_sales()
    elif choice == "8":
        update_sale_price()
    elif choice == "9":
        delete_sale()
    elif choice == "10":
        insert_dealer()
    elif choice == "11":
        View_Dealers()
    elif choice == "12":
        update_Dealer()
    elif choice == "13":
        delete_dealer()
    elif choice == "14":
        print("Exited !")
        break        
    else:
        print("Invalid choice. Please try again.")

# Closing the cursor and connection
cursor.close()
connection.close()
