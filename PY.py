import pandas as pd
from datetime import date
import csv

def main():
    print("1. User  2. Manager")
    c= input('Enter Choice : ')
    if c =="1":
        user()
    elif c =='2':
        p= input('Enter Password : ')
        if p== '3443':
            manager()
        else:
            main()
    else:
        main()
       

def user():
    print('1. Check Products.   2. Buy. 3. Cancel.  4.Exit.')
    c = input('Enter Choice :')
    if c== '1':
        cproducts()
    elif c =='2':
        buy()
    elif c=='3':
        cancel()
    elif c=='4':
        main()
    else:
        user()
def cproducts():
    l=r'C:\Users\hello\Desktop\New folder\products.csv'
    with open(l,'r')as cf:
        cw = csv.reader(cf)
        cd = pd.DataFrame(cw)
        print('|-------------------------------------|')
        for i in cd.index:
            x=list(cd.loc[i])
            print('PID : ',i)
            print('NAME : ',x[0])
            print('COST : ',x[1])
            print('REMARKS : ',x[2])
            print('|-------------------------------------|')
        cf.close()
        user()
def buy():
    p=input('Product ID: ')
    n=input('Your Name : ')
    a=input('Address : ')
    t = date.today()
    row = [p,n,a,t]
    print('Kindly Pay On Delivery')
    ol =r'C:\Users\hello\Desktop\New folder\oders.csv'
    with open(ol,'a+',newline='')as cf:
        cw = csv.writer(cf)
        cw.writerow(row)
    cf.close()
    user()
def cancel():
    p=input('Product ID : ')
    n = input('Your Name : ')
    a = input('Address : ')
    t= input('Date')
    row=[p,n,a,t]
    l = r'C:\Users\hello\Desktop\New folder\oders.csv'
    with open(l,'r+')as cf:
        cw = csv.reader(cf)
        cd = pd.DataFrame(cw)
        for i in cd.index:
            x = list(cd.loc[i])
            if row== x:
                cd.drop([i],inplace=True)
        cf.close
        with open(l,'w',newline='') as cf:
            cw=csv.writer(cf)
            for i in cd.index:
                x = list(cd.loc[i])
                cw.writerow(x)
        cf.close()
    user()
def manager():
    print('1. Add.  2. Products.    3. Delete.  4. Check Order.  5.Exit.')
    c=input('Enter Choice : ')
    if c == '1':
        add()
    elif c=='2':
        products()
    elif c=='3':
        delete()
    elif c=='4':
        
        coders()
    elif c=='5':
        main()
    else:
        manager()
def add():
    n=input('Name : ')
    c = input('Cost : ')
    d = input('Details : ')
    row = [n,c,d]
    l=r'E:\Sales Managment System\products.csv'
    with open(l,'a+',newline='')as cf:
        cw =csv.writer(cf)
        cw.writerow(row)
    cf.close()
    manager()
def products():
    l=r'C:\Users\hello\Desktop\New folder\products.csv'
    with open(l,'r')as cf:
        cw= csv.reader(cf)
        cd= pd.DataFrame(cw)
        print('|-------------------------------------|')
        for i in cd.index:
            x = list(cd.loc[i])
            print('PID : ',i)
            print('NAME : ',x[0])
            print('COST : ',x[1])
            print('REMARKS : ',x[2])
            print('|-------------------------------------|')
    cf.close()
    manager()
def delete():
    d = int(input('Enter PID : '))
    l= r'C:\Users\hello\Desktop\New folder\products.csv'
    with open(l,'r+')as cf:
        cw = csv.reader(cf)
        cd = pd.DataFrame(cw)
        cd.drop([d],inplace=True)
        cf.close()
        with open(l,'w',newline='') as cf:
            cw = csv.writer(cf)
            for i in cd.index:
                x = list(cd.loc[i])
                cw.writerow(x)
    cf.close()
    manager()
def coders():
    l=r'C:\Users\hello\Desktop\New folder\oders.csv'
    with open(l,'r')as cf:
        cw = csv.reader(cf)
        cd = pd.DataFrame(cw)
        print('|-------------------------------------|')
        for i in cd.index:
            x = list(cd.loc[i])
            print('PID : ',x[0])
            print('NAME : ',x[1])
            print('ADDRESS : ',x[2])
            print('DATE : ',x[3])
            print('|-------------------------------------|')
    cf.close()
    manager()
main() 
            

    
        
    

