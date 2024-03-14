from Person import Person
import re
from DB import db

class User(Person):
    def __init__(self):
        super().__init__()
        self.user_id = ""
        self.Total_Billings_Amount = 0

    def availAction(self):
        print("Choose Your Option:\n")
        print("1.Login\n")
        print("2.Sign_Up\n")
        print("3.Payment\n")
        print("4.Logout\n")
        
        args = int(input("Enter_your_choice:"))
        if args == 1:
            self.login()
        elif args == 2:
            self.sign_up()
        elif args == 3:
            self.payment()
        elif args == 4:
            self.logout()
        else:
            print("Invalid choice")

    def login(self):
        ph_no = str(input("Enter Your Phone Number:"))
        email_id = str(input("Enter Your Email id:"))
        self.user_id = str(ph_no + "_" + email_id)
        
        response = self.authorize(self.user_id)
        if response:
            print("Login Successful.\n")
            
            self.name = response['Name']
            self.phone = response['Phone']
            self.email = response['Email']
            self.location = response['Location']
            
            No_of_rooms=int(input("Enter Number of Rooms required: "))
            Days=int(input("Enter Number of Days: "))
            self.booking(self.user_id, No_of_rooms,Days)
        else:
            print("Login Failed")
            print("User Doesn't Exist Please Choose Option Signup\n")
            self.availAction()
            return
    
    def sign_up(self):
        self.name = str(input("Enter your name: "))
        self.phone = str(input("Enter your phone number: "))
        self.email = str(input("Enter your email: "))
        self.location = str(input("Enter your address: "))


        phone_valid=re.fullmatch(self.phn_re,self.phone)
        if phone_valid==None:
            print("Invalid Phone Number")
            self.availAction()
            return
        email_valid = re.fullmatch(self.email_re,self.email)
        if email_valid == None:
            print("Invalid Email Id")
            self.availAction()
            return
        
        if phone_valid and email_valid:
            user_id = str(self.phone + "_" + self.email)
            if user_id in db().getUsers():
                print("User Already Exist Please Choose Option Login\n")
                self.availAction()
            else:
                user_info = {
                    "Name": self.name,
                    "Email": self.email,
                    "Phone": self.phone,
                    "Location": self.location,
                    "Total_Billings_Amount": 0.0,
                }
        
                db().setUser(user_info)
                print("Sign Up Successful You can continue with you booking")
                self.availAction()
        else:
            print("Invalid Input")
            self.availAction()
            return
    
    def authorize(self,user_id):
        users = db().getUsers()
        if user_id not in users:
            return False
        else:
            return users[user_id]
        
    def booking(self,user_id,No_of_rooms,Days):
        for hotel_id, hotel in db().getHotels().items():
            for key2,value2 in hotel.items():
                print(key2,"->",value2)

            print("--------------------------------")
            ip = str(input("Enter Yes for this Hotel Else No:"))
            if ip=="Yes" and hotel["Total_Rooms"]>=No_of_rooms:
                hotel["Total_Rooms"]=hotel["Total_Rooms"] - No_of_rooms
                Total_billings_amount=No_of_rooms*Days*hotel["Price_per_Room"]
                users=db().getUsers()
                user=users[user_id]
                db().updateHotel(hotel_id, hotel)

                print("Congratulations Mrs/Ms",self.name,"your Booking is succefully made.")
                print("Your Total Billings Amount is",Total_billings_amount,"only\n")
                user['Total_Billings_Amount']=self.Total_Billings_Amount+Total_billings_amount
                db().setUser(user)
                self.availAction()
                break
            elif ip=="No":
                continue
            else:
                print("No hotel found based on your requirement\n")
                self.availAction()

    def payment(self):
        amount=float(input("Enter Amount to be paid:"))
        ph_no=str(input("Please enter your phone number:"))
        email_id=str(input("Please enter your email address:"))
        user_id=str(ph_no+"_"+email_id)
        if user_id not in db().getUsers():
            print("User Doesn't Exist")
            self.availAction()
        else:
            user=db().getUsers()[user_id]
            if user['Total_Billings_Amount']>=amount:
                user['Total_Billings_Amount']=user['Total_Billings_Amount']-amount
                print("Congratulations Mr ",user["Name"],"payment of ",amount,"is made")
                print("Reamaing amount to be paid is "+str(user['Total_Billings_Amount']))
                db().updateUser(user_id,user)
                self.availAction()
            else:
                print("Enter correct amount")
                self.availAction()
    
    def getUsers(self):
        return self.__users