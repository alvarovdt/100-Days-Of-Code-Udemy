from game_data import data
from art import logo, vs
from replit import clear
from random import randint
option_A = 0
option_B = 0
score = 0

print(logo)

def generate_options():
  global option_A, option_B
  
  option_B = randint(0,len(data)-1)
  while option_A == option_B:
    option_B = randint(0,len(data)-1)

def compare_options():
  print(f"Compare A: {data[option_A]['name']}, {data[option_A]['description']} from {data[option_A]['country']}")
  print(vs)
  print(f"Compare B: {data[option_B]['name']}, {data[option_B]['description']} from {data[option_B]['country']}")

def game():
  global option_A,option_B, score
  end_of_game = False
  option_A = randint(0,len(data)-1)
  while not end_of_game:
    
    generate_options()
    compare_options()

    choice=input("Who has more followers 'A' or 'B'? ").upper()

    if choice == "A":
      if data[option_A]['follower_count'] > data[option_B]['follower_count']:
        print("Correct")
        score+=1
        print(f"Your score is: {score}\n\n")
      else:
        clear()
        print(f"Sorry, it's incorrect, final score is: {score}")
        end_of_game=True
    else:
      if data[option_A]['follower_count'] < data[option_B]['follower_count']:
        print("Correct")
        score+=1
        print(f"Your score is: {score}\n\n")
        option_A = option_B
      else:
        clear()
        print(f"Sorry, it's incorrect, final score is: {score}")
        end_of_game= True
game()