#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: You might need to do some research in Google to figure out how to do this.

bill_total = float(input("What was the total bill? $"))
percentatge = int(input("What percentatge do you want to give? 10, 12 or 15?"))
number_of_people = int(input("How many people to split the bill?"))

bill_per_person = (bill_total / number_of_people)* (1+percentatge/100)

bill_per_person_str = format(bill_per_person, '.2f')
print(f"Each will have to pay {bill_per_person_str}")