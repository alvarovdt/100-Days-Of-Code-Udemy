from art import logo
import random


attempts=0
difficulty=""

EASY=10
HARD=5

def generate_random_number():
  return random.randint(0, 100)

def lose_an_attempt():
  global attempts,end_of_game
  attempts-=1
  if attempts == 0:
    end_of_game=True
    print("GAME OVER")

def init_attempts(nattempts):
  global attempts
  attempts=nattempts

def set_difficulty():
  global difficulty
  difficulty=input("Choose your difficulty 'easy' or 'hard': ")

  if difficulty == "easy":
    init_attempts(EASY)
  else:
    init_attempts(HARD)

def game():
  end_of_game=False
  print(logo)
  print("Welcome to the Number Guessing Game")
  print("I am thinking about a number between 0 and 100")
  
  set_difficulty()
  print(f"{difficulty} mode so {attempts} attempts")

  generated_number=generate_random_number()
  print(f"The number is: {generated_number}")
  
  while not end_of_game:
    your_number=int(input("Tell me your number: "))

    if your_number < generated_number:
      print("Your guess is too low")
      lose_an_attempt()
      print(f"You have {attempts} attempts remaining")
    elif your_number > generated_number:
      print("You guess is too high")
      lose_an_attempt()
      print(f"You have {attempts} attempts remaining")
    else:
      print("Your guessed it!")
      end_of_game=True

game()