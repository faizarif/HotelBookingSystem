from User import User
from Admin import Admin
from DB import db

print("Welcome to Exl Hotel Service\n")

repeat = True

while repeat:
    ip = int(input("Enter 1 for User 2 for Admin: "))
    while ip not in [1, 2]:
        print("Invalid Choice. Try again.")
        ip = int(input("Enter 1 for user 2 for Admin: "))

    guest = User() if ip == 1 else Admin()
    guest.availAction()

    repeat = input('Do you want to repeat? Enter y to continue.') == 'y'