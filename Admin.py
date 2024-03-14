from DB import db
from Hotel import Hotel
from Person import Person

class Admin(Person):
    def __init__(self):
        super().__init__()

    def availAction(self):
        print("Choose Your Option:\n")
        print("1.Display_User_Data\n")
        print("2.New_Hotel_Registration\n")
        print("3.Display_Hotel_information\n")
        print("4.Logout")
        args = int(input("Enter_your_choice:"))
        if args==1:
            self.display_user_data()
        elif args == 2:
            self.new_hotel_registration()
        elif args == 3:
            self.display_hotel_information()
        elif args == 4:
            self.logout()
        else:
            print("Invalid choice")

    def display_user_data(self):
        users = db().getUsers()
        for _, value in users.items():
            for key2,value2 in value.items():
                print(key2,"->",value2)
            print("--------------------------------")
        self.availAction()

    def display_hotel_information(self):
        hotels = db().getHotels()
        
        for _, value in hotels.items():
            for key2, value2 in value.items():
                print(key2, "->", value2)
            print("--------------------------------")

        self.availAction()

    def new_hotel_registration(self):
        hotel = Hotel()
        hotel.new_hotel_registration()

        self.availAction()

    def login(self):
        pass
        # if self.authorize(self.user_id):
        #     No_of_rooms=int(input("Enter Number of Rooms reuired: "))
        #     Days=int(input("Enter Number of Days: "))
        #     self.booking(self.user_id, No_of_rooms,Days)
        # else:
        #     print("Login Failed")
        #     print("User Doesn't Exist Please Choose Option Signup\n")
        #     self.availAction()
        #     return
    
    def sign_up(self):
        pass
        
    def authorize(self,user_id):
        if user_id not in self.admin:
            return False
        else:
            return True
