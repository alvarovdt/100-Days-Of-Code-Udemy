import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Welcome to PyRockPaperScissors game!")
my_choice= int(input("Type 0 for Rock, 1 for Paper and 2 for Scissors: "))

list_rps = [rock,paper,scissors]
list_str_rps = ["rock","paper","scissors"]
computer_choice = random.randint(0,2)

print(f"\n\nYour played: {list_str_rps[my_choice]}\n {list_rps[my_choice]}")
print(f"Bot played: {list_str_rps[computer_choice]}\n {list_rps[computer_choice]}")
if my_choice == computer_choice:
  print("It's a draw")
elif my_choice == 0 and computer_choice == 2:
  print("You win");
elif my_choice == 0 and computer_choice == 1:
  print("You lose")
elif my_choice == 1 and computer_choice == 0:
  print("You win");
elif my_choice == 1 and computer_choice == 2:
  print("You lose")
elif my_choice == 2 and computer_choice == 0:
  print("You lose")
elif my_choice == 2 and computer_choice == 1:
  print("You win");