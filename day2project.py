print("Welcome to the tip calculator!")
bill=float(input("What is the total Bill? $"))
tip_percent=int(input("How much % tip would you like to give? "))
people=int(input("How many people to split the bill? "))
bill_per_person = round(((bill + (tip_percent/100*bill))/people),2)
print(f"Each person should pay: ${bill_per_person}")

