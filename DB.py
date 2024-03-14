import uuid
class db(object):
    __users = {
        "7488261191_faiz@gmail.com": {
            "Name":"Faizan Arif",
            "Email":"faiz@gmail.com",
            "Phone":7488261191,
            "Location":"Noida",
            "Total_Billings_Amount":1000.0,
        }
    }
    uniqueid = uuid.uuid1()
    __hotels = {
        str(uniqueid):
        {
            "Hotel_Name":"Holiday Inn",
            "Hotel_Location":"Noida",
            "Hotel_Amenities":"Tv,Ac,Parking",
            "Total_Rooms":11,
            "Price_per_Room":3200.0,
        }
    }
    __admins={}

    __bookings={}

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(db, cls).__new__(cls)
        return cls.instance
    
    def getUsers(self):
        return self.__users
    
    def getAdmin(self):
        return self.__admins
    
    def getHotels(self):
        return self.__hotels

    def getBookings(self):
        return self.__bookings
    
    def setUser(self,user):
        user_id = str(str(user["Phone"]) + "_" +str(user["Email"]))
        self.__users[user_id] = user
    
    def setHotel(self,hotel):
        hotel_id=str(uuid.uuid1())
        self.__hotels[hotel_id] = hotel

    def updateHotel(self, hotel_id, hotel):
        self.__hotels[hotel_id] = hotel
    
    def Bookings(self, booking):
        booking_id=str(uuid.uuid1())
        self.__bookings[booking_id] = booking

    def updateUser(self,user_id,user):
        self.__users[user_id] = user
    