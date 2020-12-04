from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)

auctioners_d={}
end_of_bid= False
print("Welcome to the Secret auction program.")

while end_of_bid == False:
  
  name=input("What is your name? ");
  bid=int(input("What is your bid? $"))
  another_bid= input("Is there any other bidders? type 'yes' or 'no' ").lower()
  auctioners_d[name]=bid;
  if (another_bid == "no"):
    end_of_bid= True
    clear()
  else:
    clear()

#print(auctioners_d)
max_bet=0
name=""
for a in auctioners_d:
  if int(auctioners_d[a]) > max_bet:
    max_bet=auctioners_d[a]
    name= a

print(f"The max bidder is {name} with a bet of ${max_bet}")