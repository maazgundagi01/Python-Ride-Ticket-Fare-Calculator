print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print(f"Your ticket is ${bill}")
    elif age <= 18:
        bill = 7
        print(f"Your ticket is ${bill}")
    else:
        bill = 10
        print(f"Your ticket is ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
    exit()

photo_charge = 0
photo_answer = input("Would you like a photo service for extra price of $3?(type y/yes or n/no)").lower
if photo_answer == "y" or "yes":
    photo_charge = photo_charge + 3
    print("you have chosen to opt-in for the photo service")
elif photo_answer == "n" or "no":
    photo_charge = photo_charge + 0
    print("you have chosen to opt-in for the photo service")

print(f"Your total bill is Ticket(${bill})  + Extra Charge(${photo_charge}) = ${bill}")
