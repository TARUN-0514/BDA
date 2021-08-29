def userHome():
    #print("Here we'll display what admin can see after login")
    userHome=True
    while userHome:
        choice = input(" \n1.Blood Search \t2.Donation \t3.Availabe blood \t4.Logout\n\nPlease enter your choice: ")
        if choice == "1":
            searchBlood()
        elif choice == "2":
            donateBlood()
        elif choice == "3":
            bloodList()
        elif choice == "4":
            break
        else:
            print("Select only given options")
            print("Please try again")

def searchBlood():
    print("Search by blood group: ")
    bloodgroupFlag=True
    while bloodgroupFlag:
        print("\nSELECT BLOOD GROUP AS GIVEN BELOW TO SEARCH: ")
        choice1=input("\n1.A+ \t2.B+ \t3.O+ \t4.AB+ \t5.A- \t6.B- \t7.O- \t8.AB-\n")
        if choice1 == "1":
            bloodGroup="A+"
            break
        elif choice1 == "2":
            bloodGroup="B+"
            break
        elif choice1 == "3":
            bloodGroup="O+"
            break
        elif choice1 == "4":
            bloodGroup="AB+"
            break
        elif choice1 == "5":
            bloodGroup="A-"
            break
        elif choice1 == "6":
            bloodGroup="B-"
            break
        elif choice1 == "7":
            bloodGroup="O-"
            break
        elif choice1 == "8":
            bloodGroup="AB-"
            break
        else:
            print("Select only given options")
            print("Please try again")
    f=open("Users_Data.txt",'r')
    userData = f.read()
    userData = userData.split()
    if bloodGroup in userData:
        firstNameIndex = userData.index(bloodGroup)-3
        lastNameIndex = userData.index(bloodGroup)-2
        numberIndex = userData.index(bloodGroup)-1
        firstName = userData[firstNameIndex]
        lastName = userData[lastNameIndex]
        number = userData[numberIndex]
        print(firstName+" "+lastName+", "+number+" is a donor with the selected blood group.")
    else:
        print("No donors available at the moment.")


def donateBlood():
    pass

def bloodList():
    print("Userdatabase: with each field seperated by a space\n")
    print(""" First  Last  Phone  Blood\n Name   Name  Number Group\n""")
    with open('Users_Data.txt') as f:
        contents = f.read()
        print(contents)
