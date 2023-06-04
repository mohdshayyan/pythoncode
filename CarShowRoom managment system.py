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

# Menu loop
while True:
    print("\n                                                           \ CAR SHOWROOM MANAGEMENT SYSTEM /\n ")
    print("                                                           (1.) Create Table                              (2.) Insert Car")
    print("                                                           (3.) Get All Cars                              (4.) Update Car Price")
    print("                                                           (5.) Delete Car                                 (6.) Exit\n")


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
        print("Exited !")
        break
    else:
        print("Invalid choice. Please try again.")

# Closing the cursor and connection
cursor.close()
connection.close()
