"""class donor:
    def getData(self, name, age, bloodGroup, contact, address):
        donor.name = name
        donor.ageString = age
        donor.bloodGroup=bloodGroup
        donor.contactString = contact
        donor.address = address"""


def reg(info1):
    print("FOLLOW THE STEPS FOR THE FURTHER REGISTRATION :")
    firstName = input("ENTER THE FIRST NAME OF THE DONOR : ")

    f = open("Users_Data.txt",'w')
    info1 = info1 + " " +firstName
    f.write(info1)

    lastName = input("ENTER THE LAST NAME OF THE DONOR : ")

    f = open("Users_Data.txt",'w')
    info1 = info1 + " " +lastName
    f.write(info1)
    
    get_age(info1)
    
    contact = int(input("ENTER THE CONTACT NUMBER OF THE DONOR : "))

    contactString=str(contact)
    f = open("Users_Data.txt",'w')
    info1 = info1 + " " +contactString
    f.write(info1)
    
    blood_group(info1)

    print("\n\nGO THROUGH THE FOLLOWING QUESTIONAIRE TO COMPLETE THE APPLICATION PROCESS :(Answer in yes or no)")
    Q1=input("\n1.Have you taken any painkillers, anti-inflammatories or aspirin (including Ecotrin)?\n2.Have you had a cold, flu, sore throat, fever, infection, open wound or allergies?\n3.Have you had an immunisation or vaccination?\n4.Have you taken part in a drug trial, vaccine trial, or clinical research?\n5.Heart (e.g. stents), lung or circulatory problems (eg. clots) or a bleeding disorder?\n6.Cancer, skin cancer (melanoma, basal cell carcinoma, squamous cell carcinoma) or leukaemia\n7.Diabetes, asthma, tuberculosis (TB) or kidney disease\n8.Any other serious illnesses, severe allergic reactions, tropical diseases or used medication not mentioned above\n9.Has your doctor advised you to donate blood to treat a medical condition such as high iron, ‘thick blood’,polycythaemia, haemochromatosis\n")
    if Q1 == ("YES"):
      print("SORRY YOUR APPLICATION IS REJECTED")
    elif Q1 == ("NO"):
      print("YOUR APPLICATION HAS BEEN CONSIDERED PLEASE GO THOROUGH USER LOGIN FOR REGISTRATION")    
    else:
      print("PLEASE ENTER YES OR NO ")

def get_age(info1):
    while True:
        age = int(input("Enter age: "))
        try:
            checker = age
            if checker >= 21 :
                print("Access Granted!")
                break
            else:
                print("Access Denied! Underage")
        except ValueError:
            print("Amount must be a number, try again")
    return checker

def blood_group(info1):
    
    bloodgroupFlag=True
    while bloodgroupFlag:
        print("\nCHOOSE YOUR BLOOD GROUP AS GIVEN BELOW:")
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
    print("\nBlood Group Chosen: "+bloodGroup)
    f = open("Users_Data.txt",'w')
    info1 = info1 + " " +bloodGroup+ "\n"
    f.write(info1)

