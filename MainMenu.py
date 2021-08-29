#Menu for Blood Donation system
import sys
from AdminHome import *
from UserHome import *
from BD_PRO import *
from mail import *

def main():
    print("******************Welcome to XYZ Blood Donation System*******************")
    menu()


def menu():

    app=True
    while app:
        choice = input("""
                          1: Registeration Form
                          2: Register for an account (Once registration form is filled)
                          3: Already registered? Login
                          4: Rare Blood group requests (in development)
                          5: Exit Application

                          Please enter your choice: """)

        if choice == "1":
            print("Register")
            f = open("Users_Data.txt",'r')
            info1 = f.read()
            f.close()
            reg(info1)
        elif choice == "2":
            register()
        elif choice == "3":
            login()
        elif choice == "4":
            
            pass
            #Menu option 4
        elif choice=="5":
            sys.exit()
        else:
            print("Select only given options")
            print("Please try again")


def register():
    print("Create an account to use our application!:\n")
    name = str(input("Userame(no spaces): "))
    password = str(input("Password: "))
    f = open("User_Login_Data.txt",'r')
    info = f.read()
    if name in info:
        return "Name Unavailable. Please Try Again"
    f.close()
    f = open("User_Login_Data.txt",'w')
    info = info + " " +name + " " + password
    f.write(info)
    
    #applicationForm() function
    
def login():

    login=True
    while login:
        choice = input(" \n\n1.Login as User \t2.Login as Admin\t3.Go Back\n\nPlease enter your choice: ")
        if choice == "1":
            loginUser()
        elif choice == "2":
            loginAdmin()
        elif choice == "3":
            break
        else:
            print("Select only given options")
            print("Please try again")

def loginUser():
        
    print("Please enter")
    name=str(input("User Name: "))
    password=str(input("Password: "))
    
    f = open("User_Login_Data.txt",'r')
    userData = f.read()
    userData = userData.split()
    if name in userData:
        passwordIndex = userData.index(name)+1
        userPassword = userData[passwordIndex]
        if userPassword == password:
            print("Welcome back,"+ name +"\n\n")
            userHome()
        else:
            print("Incorrect password. Try again")
    else:
        print("Username invalid.")
            
def loginAdmin():

    print("Please enter details")
    name=str(input("User Name: "))
    password=str(input("Password: "))

    f=open("Admin_Data.txt",'r')
    adminData = f.read()
    adminData = adminData.split()
    if name in adminData:
        passwordIndex = adminData.index(name)+1
        adminPassword = adminData[passwordIndex]
        if adminPassword == password:
            print("Welcome back admin,"+ name+ "\n")
            adminHome()
        else:
            print("Incorrect password. Try again")
    else:
        print("Invalid admin name.")
        
    
#the program is initiated, so to speak, here
main()
