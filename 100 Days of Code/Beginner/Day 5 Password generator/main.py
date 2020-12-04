#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password = []
total_char = nr_letters+nr_symbols+nr_numbers
current_char=0;
current_symbol=0;
current_number=0;
for generator in range(0,total_char):
  letter_symbol_number = random.randint(0,2)
  if current_char >= nr_letters or current_symbol >= nr_symbols or current_number >= nr_numbers:
    letter_symbol_number=0
  if letter_symbol_number==0:
    if current_char >= nr_letters:
      letter_symbol_number=1
    else:
      password.append(letters[random.randint(0,len(letters)-1)])
      current_char +=1
  if letter_symbol_number==1:
    if current_symbol >= nr_symbols:
      letter_symbol_number=2
    else:
      password.append(symbols[random.randint(0,len(symbols)-1)])
      current_symbol +=1
  if letter_symbol_number==2:
        password.append(numbers[random.randint(0,len(numbers)-1)])
        current_number +=1

print((password))
print("".join(password))