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
    elif age>=45 and age<=55:
        print("Everything is ok, have a free ride")
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


print("Welcome to python pizza deliveries")
size = input("What size pizza do you need? S, M or L?: ")
pepperoni = input("Do you need pepperoni in your pizza? Y or N?: ")
extra_cheese = input("Do you need extra cheese? Y or N?: ")
final_bill=0
if size=="S":
    final_bill+=15
    if pepperoni == "Y":
        final_bill +=2
elif size=="M":
    final_bill+=20
    if pepperoni == "Y":
        final_bill +=3
elif size=="L":
    final_bill+=25
    if pepperoni == "Y":
        final_bill +=5
else:
    print("You typed a wrong input")
if extra_cheese=="Y":
    final_bill+=1
print(f"Your final bill is {final_bill}")
