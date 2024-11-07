print("Welcome to the rollercoaster ride!")
bill=0
height=float(input("What is your height in centimeters? "))
if height>=120:
    age=int(input("What is your age? "))
    if age<=12:
        bill=5
        print(f"You can take a ride, your ticket price is ${bill}")
    elif age<=18:
        bill=7
        print(f"You can take a ride, your ticket price is ${bill}")
    else:
        bill=12
        print(f"You can take a ride, your ticket price is ${bill}")
    want_photo=input("Do you want a Photo? Type Yes or No: ")
    if want_photo=="Yes":
        print(f"Your ticket price is ${bill+3}")
    else:
        print(f"Your ticket price is ${bill}")
else:
    print("Sorry, you cannot take a ride")

print(10%3)

print("Check Even or Odd")
number=int(input("Enter a number "))
if number%2==0:
    print("The number you have entered is Even")
else:
    print("The number you have entered is Odd")