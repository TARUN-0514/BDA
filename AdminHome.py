def adminHome():
    #print("Here we'll display what admin can see after login")
    adminHome=True
    while adminHome:
        choice = input(" \n1.View User Database \t2.Add Hospitals/Donation Camps\t3.Blood requests \t4.Blood samples collected from specific blood banks \t5.Rare blood group samples collected from differnt blood banks\t6.Logout\n\nPlease enter your choice: ")
        if choice == "1":
            userDatabase()
        elif choice == "2":
            addHospitals()
        elif choice == "3":
            requestList()
        elif choice == "4":
            sbb()
        elif choice == "5":
            rbsd()
        elif choice == "6":
            break
        else:
            print("Select only given options")
            print("Please try again")
    

def userDatabase():
    print("Userdatabase: with each field seperated by a space\n")
    print(""" First  Last  Phone  Blood\n Name   Name  Number Group\n""")
    with open('Users_Data.txt') as f:
        contents = f.read()
        print(contents)

def addHospitals():
    while True:
       choice = input("\n1.Add hospital \t2.Add blood camps")
       if choice == "1":
           addh()
           break
       elif choice == "2":
           addc()
           break
       else:
           print("Select only given options")
           print("Please try again")

def requestList():
    choice = input("Requests from user :")
    f= open("User_Data.txt", 'r')
    User_Data = f.read()
    User_Data = User_Data.split()

    if choice in User_Data:
        print("Approving blood request")
        userHome()
    else:
        print("Sorry invalid option")

def addh():
        choice = input("Add hospital : ")
        f=open("hospitalinfo.txt",'r')
        info=f.read()
        if choice in info:
            return "Name already exits"
        f.close()
        f = open("hopitalinfo.txt", 'w')
        info = info + ""+choice +""
        f.write(info)
def addc():
    choice = input("Add blood camps")
    f=open("campsinfo.txt",'w')
    info=f.read()
    if choice in info:
        return "Name already exits"
    f.close()
    f = open("campsinfo.txt",'w')
    info=info + ""+choice +""
    f.write(info)

def sbb():
    choice = input("Blood group from differnt hospitals")
    f=open("hospitalinfo.txt", 'r')
    info=f.read()
    if choice in info:
        return "Blood sample from hospital xyz is verified "
    f.close()
    f=open("campsinfo.txt",'r')
    info=f.read()
    if choice in info:
        return "Blood sample from blood camp xyz is verified"
    f.close()

def rbsd():
    choice = input("Rare group from specific hospitals")
    f=open("User_Data.txt",'r')
    info=f.read()
    if choice in info:
        return "Rare blood group available in our deposits"
    f.close()
