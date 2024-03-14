import uuid
from DB import db
class Hotel():
    def __init__(self):
        self.hotel_id=""
        self.hotel_name=""
        self.hotel_location=""
        self.hotel_amenities=""
        self.total_rooms=""
        self.price_per_room=""

    def new_hotel_registration(self):
        self.hotel_name=str(input("Enter Your Hotel Name: "))
        self.hotel_location=str(input("Enter Your Hotel Location: "))
        self.hotel_amenities=str(input("Enter Your Amenities: "))
        self.total_rooms=int(input("Enter Your Total Rooms: "))
        self.price_per_room=float(input("Enter Your Price per Room: "))
        
        hotel_info = {
            "Hotel_Name":self.hotel_name,
            "Hotel_Location":self.hotel_location,
            "Hotel_Amenities":self.hotel_amenities,
            "Total_Rooms":self.total_rooms,
            "Price_per_Room":self.price_per_room,
        }
        
        db().setHotel(hotel_info)
        print("Hotel Registration Successful")