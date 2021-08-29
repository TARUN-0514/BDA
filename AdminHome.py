def adminHome():
    #print("Here we'll display what admin can see after login")
    adminHome=True
    while adminHome:
        choice = input(" \n\n\n1.View User Database \t2.Add Hospitals/Donation Camps\t3.Blood requests \t4.Logout\n\nPlease enter your choice: ")
        if choice == "1":
            userDatabase()
        elif choice == "2":
            addHospitals()
        elif choice == "3":
            requestList()
        elif choice == "4":
            break
        else:
            print("Select only given options")
            print("Please try again")
    

def userDatabase():
    pass

def addHospitals():
    pass

def requestList():
    pass
