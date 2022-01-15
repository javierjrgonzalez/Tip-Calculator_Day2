#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
#bill = (150.00 / 5) * 1.12 
#rounded_bill = "{:.2f}".format(bill)
#print(rounded_bill)

print("Welcome to the tip calculator.")
total = input("What was the total bill? $")
total = float(total)
tip = input("What percentage tip would you like to give? ")
tip = float(tip)
tip_to_be_added = (total * (tip/100))
cost = (total + tip_to_be_added)
people = input("How many people to split the bill? ")
people = int(people)
pay = (cost / people)
rounded_pay = "{:.2f}".format(pay)
print(f"Each person should pay: ${rounded_pay}")
