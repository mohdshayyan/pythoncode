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
    print("                                                 ---| Welcome to  School System by Shayyan|---\n")
    print("(1.) Add New   record                                          (2.) View  details")
    print("(3.) Update   details                                            (4.) Delete   details")
    print("(5.) Add new   record                                               (6.) View   details")    
    print("(7.) Update   details                                                 (8.) Delete   details")
    print("(9.) Add   deposit details                                           (10.) View   datails")
    print("(11.) Update   datails                                                  (12.) Delete   datails                     (13.) Exit")










