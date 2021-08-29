def reg():
    print("FOLLOW THE STEPS FOR THE FURTHER REGISTRATION :")


class donor:
    def getData(self, name, age, blood_group, contact, address):
        donor.name = name
        donor.age = age
        donor.blood_group=blood_group
        donor.contact = contact
        donor.address = address


name = input("ENTER THE NAME OF THE DONOR : ")


def get_age():
    while True:
        Age = input("Enter age: ")
        try:
            checker = int(Age)
            if checker >= 21 :
                print("Access Granted!")
                break
            else:
                print("Access Denied! Underage")
        except ValueError:
            print("Amount must be a number, try again")
    return checker
get_age()

contact = int(input("ENTER THE CONTACT OF THE DONOR : "))
address = input("ENTER THE ADDRESS OF THE DONOR :")


def blood_group():
        choice1=input("\n\n\n1.A+ \t2.B+ \t3.O+ \t4.AB+ \t5.A- \t6.B- \t7.O- \t8.AB-")
        print("CHOOSE NO. ACCORDING TO YOUR BLOOD GROUP : ", choice1)

print("GO THROUGH THE FOLLOWING QUTIONER TO COMPLETE THE APPLICATION PROCESS : ")

Q1=input("1.Have you taken any painkillers, anti-inflammatories or aspirin (including Ecotrin)?\n2.Have you had a cold, flu, sore throat, fever, infection, open wound or allergies?\n3.Have you had an immunisation or vaccination?\n4.Have you taken part in a drug trial, vaccine trial, or clinical research?\n5.Heart (e.g. stents), lung or circulatory problems (eg. clots) or a bleeding disorder?\n6.Cancer, skin cancer (melanoma, basal cell carcinoma, squamous cell carcinoma) or leukaemia\n7.Diabetes, asthma, tuberculosis (TB) or kidney disease\n8.Any other serious illnesses, severe allergic reactions, tropical diseases or used medication not mentioned above\n9.Has your doctor advised you to donate blood to treat a medical condition such as high iron, ‘thick blood’,polycythaemia, haemochromatosis\n")
if Q1 == ("YES"):
  print("SORRY YOUR APPLICATION IS REJECTED")
elif Q1 == ("NO"):
  print("YOUR APPLICATION HAS BEEN CONSIDERED PLEASE GO THORUOGH USER LOGIN FOR REGISTRATION")    
else:
  print("PLEASE ENTER YES OR NO ")
