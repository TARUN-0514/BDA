def userHome():
    #print("Here we'll display what admin can see after login")
    userHome=True
    while userHome:
        choice = input(" \n\n\n1.Blood request \t2.Donation \t3.Availabe blood \t4.Logout\n\nPlease enter your choice: ")
        if choice == "1":
            requestBlood()
        elif choice == "2":
            donateBlood()
        elif choice == "3":
            bloodList()
        elif choice == "4":
            break
        else:
            print("Select only given options")
            print("Please try again")

def requestBlood():
    pass

def donateBlood():
    pass

def bloodList():
    pass
