import pandas as pd
import os
print("\t\t\t +---------------------------------------------------------------+")
print("\t\t\t| Welcome To Patient Managment System by Shayyan |")
print("\t\t\t +---------------------------------------------------------------+")
#        PATIENT MANAGEMENT MENU               
def pmenu():
    #os.system("cls")
    
    input("Press ENTER KEY to continue.....")
    print("\t\t\t           +-----------------------------------+")
    print("\t\t\t           |     PATIENT MAIN MENU      |")
    print("\t\t\t           +-----------------------------------+")
    print("\t\t\t           | 1. New Patient Registration |")
    print("\t\t\t           | 2. Update Patient Details    |")
    print("\t\t\t           | 3. Remove Patient                 |")
    print("\t\t\t           | 4. Search Patient by PNo     |")
    print("\t\t\t           | 5. All Patient List                  |")
    print("\t\t\t           | 6. EXIT                                   |")
    print("\t\t\t           +----------------------------------+")
    print()



#          NEW PATIENT REGISTRATION            
def patRegister():
    patdf = pd.read_csv("csvfile\\patientnew.csv", index_col = 0)
    rno = len(patdf)
    #print(rno)
    while True:
        print("Please Enter Patient Details")
        pid = int(input("Patient Id : "))
        if serPatientbyId(pid)> 0 :
            print("Duplicate Patient Id, ENTER A VALID PATIENT ID")        
        else:
            break
        
    name = input("Name : ")
    age = input("Age : ")
    weight = input("Weight : ")
    gender = input("Gender : ")
    address = input("Address : ")
    phoneno = input("Phone Number : ")
    disease = input("Disease : ")
    patdf.loc[pid,:] = [pid,name,age,weight,gender,address,phoneno,disease]
    #print(patdf)
    patdf.to_csv("csvfile\\patientnew.csv", mode='w')

#              UPDATE PATIENT                   
def patUpdate():
    patdf = pd.read_csv("csvfile\\patientnew.csv", index_col = 0)
    pid = int(input("Enter Patient Id to Update: "))

    if serPatientbyId(pid)> 0 :
        print("Patient Found")
        print("Enter details to update patient")
        name = input("Name : ")
        age = input("Age : ")
        weight = input("Weight : ")
        gender = input("Gender : ")
        address = input("Address : ")
        phoneno = input("Phone Number : ")
        disease = input("Disease : ")
        patdf.loc[patdf.loc[patdf['pid'] == pid].index,:] = [pid,name,age,weight,gender,address,phoneno,disease]        
        patdf.to_csv("csvfile\\patientnew.csv", mode='w')
        print("Updated Successfully")
    else:
        print("Invaid Patient ID")


#                    REMOVE PATIENT            
def patRemove():
    patdf = pd.read_csv("csvfile\\patientnew.csv", index_col = 0)
    pid = int(input("Enter Patient Id to Delete: "))
    patdf.drop(patdf.loc[patdf['pid']==pid].index, inplace=True) #Remove
    
    patdf.to_csv("csvfile\\patientnew.csv", mode='w')    
    
#              DISPLAY ALL PATIENT              
def dispPatient():
    patdf = pd.read_csv("csvfile\\patientnew.csv", index_col= 1)
    print(patdf)


#              SEARCH PATIENT BY ID            
def serPatientbyId(pid):
    patdf = pd.read_csv("csvfile\\patientnew.csv", index_col = 0)
    if patdf.empty:
        return 0
    else:
        return len(patdf.loc[patdf['pid'] == pid])


#           GET PATIENT  DF BY ID              
def getPatient(pid):
    patdf = pd.read_csv("csvfile\\patientnew.csv", index_col = 0)
    if patdf.empty:
        return "Invalid ID"
    else:
        return patdf.loc[patdf['pid'] == pid]


#           GET PATIENT  NAME BY ID            
def getPatientName(pid):
    patdf = pd.read_csv("csvfile\\patientnew.csv", index_col = 0)
    if patdf.empty:
        return "Invalid ID"
    else:
        return patdf.iat[0,1]



#              SEARCH PATIENT BY NAME          
def serPatientbyName():
    global patdf
    patdf = pd.read_csv("csvfile\\patientnew.csv", index_col = 0)
    pname  = input("Patient Name :: ")
    print(patdf.loc[patdf['name'] == pname])

def serPatientbyIDPrint():
    global patdf
    patdf = pd.read_csv("csvfile\\patientnew.csv", index_col = 0)
    tid  = int(input("Patient ID :: "))
    print(patdf.loc[patdf['pid'] == tid])


#              GET CHOICE                      
def getchoice():
    while True:
        pmenu()
        ch = input("\t\t\t Enter Your Choice :: ")
        if ch == '1':
            print("PATIENT REGISTRATION")
            patRegister()
        elif ch=='2':
            print("PATIENT UPDATION")
            patUpdate()
        elif ch=='3':
            print("PATIENT DELETION")
            patRemove()
        elif ch=='4':
            print("PATIENT SEARCHING")
            print("1. By ID")
            print("2. By Name")
            ch = input("Enter your search criteria :: ")
            if ch == '1':
                serPatientbyIDPrint()
                print()
                print()
            elif ch == '2':
                serPatientbyName()
                print()
                print()
        elif ch=='5':
            print("\t\t                                  LIST OF PATIENTS")
            print("----------------------------------------------------------------------------------------------------------------------------------------")
            dispPatient()
        elif ch == '6':
            break
        else:
            print("INVALID CHOICE")

        input("Press ENTER KEY to continue.....")

#main

getchoice()
