import re
import uuid

class App:
    def __init__(self):
        self.user={}
        self.hotel={}

        uniqueid = uuid.uuid1()
        hotel_id=str(uniqueid)
        hotel_info={
                    "Hotel_Name":"Holiday Inn",
                    "Hotel_Location":"Noida",
                    "Hotel_Amenities":"Tv,Ac,Parking",
                    "Total_Rooms":11,
                    "Price_per_Room":3200.0,
                    }
        
        self.hotel[hotel_id]=hotel_info

        user_info={"Name":"Faizan Arif",
                   "Email":"FaizanArif@1829@gmail.com",
                   "Phone":7488261191,
                   "Location":"Noida",
                   "Total_Billings_Amount":1000.0,
        }
        
        self.user["7488261191_faizarif1829@gmail.com"]=user_info

       
        print("Initialized")

    def Authorize(self,user_id):
        if user_id not in self.user:
            return False
        else:
            return True
    
    def Login(self,user_id):
        if self.Authorize(user_id):
            No_of_rooms=int(input("Enter Number of Rooms reuired: "))
            Days=int(input("Enter Number of Days: "))
            self.Booking(user_id,No_of_rooms,Days)
        else:
            print("Login Failed")
            print("User Doesn't Exist Please Choose Option Signup\n")
            self.switch()
            return
            
    def sign_up(self):
        ph_no=str(input("Enter Your Phone Number:"))
        x1=re.fullmatch(self.phn,ph_no)
        if x1==None:
            print("Invalid Phone Number")
            self.switch()
            return
        email_id=str(input("Enter Your Email id:"))
        x2=re.fullmatch(self.email,email_id)
        if x2==None:
            print("Invalid Email Id")
            self.switch()
            return
        
        if x1 and x2:
            user_id=str(ph_no+"_"+email_id)
            if user_id in self.user:
                print("User Already Exist Please Choose Option Login\n")
                self.switch()
            else:
                user_name=str(input("Enter Your Name: "))
                user_location=str(input("Location:"))

                user_info={"Name":user_name,
                        "Email":email_id,
                        "Phone":ph_no,
                        "Location":user_location,
                        "Total_Billings_Amount":0.0,
                        }
        
                self.user[user_id]=user_info
                print("Sign Up Successful You can continue with you booking")
                self.switch()
        else:
            print("Invalid Input")
            self.switch()
            return
        
    def payment(self,amount):
        ph_no=str(input("Please enter your phone number:"))
        email_id=str(input("Please enter your email address:"))
        user_id=str(ph_no+"_"+email_id)
        if user_id not in self.user:
            print("User Doesn't Exist")
            self.switch()
        else:
            dict2=self.user[user_id]
            if dict2['Total_Billings_Amount']>=amount:
                dict2['Total_Billings_Amount']=dict2['Total_Billings_Amount']-amount
                print("Congratulations Mr ",dict2['Name'],"payment of ",amount,"is made")
                print("Reamaing amount to be paid is "+str(dict2['Total_Billings_Amount']))
                self.switch()
            else:
                print("Enter correct amount")
                self.switch()

    def new_hotel_registration(self):
        uniqueid = uuid.uuid1()
        hotel_id=str(uniqueid)
        hotel_name=str(input("Enter Your Hotel Name: "))
        hotel_location=str(input("Enter Your Hotel Location: "))
        hotel_amenities=str(input("Enter Your Amenities: "))
        total_rooms=int(input("Enter Your Total Rooms: "))
        price_per_room=float(input("Enter Your Price per Room: "))

        hotel_info={
                    "Hotel_Name":hotel_name,
                    "Hotel_Location":hotel_location,
                    "Hotel_Amenities":hotel_amenities,
                    "Total_Rooms":total_rooms,
                    "Price_per_Room":price_per_room,
                    }
        
        self.hotel[hotel_id]=hotel_info
        print("Hotel Registration Successful")
        self.switch()

    def switch(self):
        print("Welcome to Exl Hotel Service\n")
        ip = int(input("Enter 1 for user 2 for Admin:"))
        
        if ip == 1:
            print("Choose Your Option:\n")
            print("1.Login\n")
            print("2.Sign_Up\n")
            print("3.Payment\n")
            args = int(input("Enter_your_choice:"))
            if args == 1:
                ph_no=str(input("Enter Your Phone Number:"))
                email_id=str(input("Enter Your Email id:"))
                user_id=str(ph_no+"_"+email_id)
                app.Login(user_id)
            elif args == 2:
                app.sign_up()
            elif args == 3:
                amount=float(input("Enter Amount to be paid:"))
                app.payment(amount)
            else:
                print("Invalid choice")
            
        elif ip==2:
            print("Choose Your Option:\n")
            print("1.Display_User_Data\n")
            print("2.New_Hotel_Registration\n")
            print("3.Display_Hotel_information\n")
            args = int(input("Enter_your_choice:"))
            if args==1:
                app.display_user_data()
            elif args == 2:
                app.new_hotel_registration()
            elif args == 3:
                app.display_hotel_information()
            else:
                print("Invalid choice")
        else:
            print("Invalid choice")

    def display_hotel_information(self):
        for key,value in self.hotel.items():
            for key2,value2 in value.items():
                print(key2,"->",value2)
            print("--------------------------------")
        self.switch()
        
    def Booking(self,user_id,No_of_rooms,Days):
        for key,value in self.hotel.items():
            for key2,value2 in value.items():
                print(key2,"->",value2)
            print("--------------------------------")
            ip =str(input("Enter Yes for this Hotel Else No:"))
            if ip=="Yes" and value["Total_Rooms"]>=No_of_rooms:
                value["Total_Rooms"]=value["Total_Rooms"]-No_of_rooms
                Total_billings_amount=No_of_rooms*Days*value["Price_per_Room"]
                print("Congratulations Mrs/Ms",self.user[user_id]["Name"],"your Booking is succefully made.")
                print("Your Total Billings Amount is",Total_billings_amount,"only\n")
                self.user[user_id]["Total_Billings_Amount"]=self.user[user_id]["Total_Billings_Amount"]+Total_billings_amount
                self.switch()
                break
            elif ip=="No":
                continue
            else:
                print("No hotel found based on your requirement\n")
                self.switch()

        

    def display_user_data(self):
        for key,value in self.user.items():
            for key2,value2 in value.items():
                print(key2,"->",value2)
            print("--------------------------------")
        self.switch()


if __name__ == "__main__":
    app=App()
    app.switch()

    

    







