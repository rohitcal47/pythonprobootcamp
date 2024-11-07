print("Welcome to the rollercoaster ride!")
height=float(input("What is your height in centimeters? "))
if height>=120:
    age=int(input("What is your age? "))
    if age<=12:
        print("You can take a ride, your ticket price is $5")
    elif age<=18:
        print("You can take a ride, your ticket price is $7")
    else:
        print("You can take a ride, your ticket price is $12")
else:
    print("Sorry, you cannot take a ride")

print(10%3)

print("Check Even or Odd")
number=int(input("Enter a number "))
if number%2==0:
    print("The number you have entered is Even")
else:
    print("The number you have entered is Odd")