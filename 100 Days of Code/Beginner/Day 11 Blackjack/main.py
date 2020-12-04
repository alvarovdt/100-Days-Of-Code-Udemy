from art import logo
from replit import clear
import random
cards = ['A','2','3','4','5','6','7','8','9','10','J','Q','K'];

my_cards = []
dealer_cards = []

my_score=0
dealer_score=0

total_cards = len(cards)
playing_cards = 0
playing_deck=[]

end_of_game=False
play_again= True

n_decks=0

print(logo)

def calculate_card(list_of_cards):
  total=0
  number_of_a=0
  for card in list_of_cards:
    if card == 'J' or card == 'Q' or card=='K':
      total+=10
    elif card=='A':
      number_of_a+=1
    else:
      total += int(card)
  if number_of_a > 0:
    if total + 11 * number_of_a <= 21:
      total += 11 * number_of_a
    else:
      total += number_of_a
  return total

def deal_cards(who, number_of_cards):
  for _ in range(number_of_cards):
      if who=="player":
        my_cards.append(playing_deck.pop(0))
      else:
        dealer_cards.append(playing_deck.pop(0))
  




n_decks= int(input("How many decks do you want to play with? "))


for _ in range(n_decks*4):
  playing_deck += cards
  playing_cards += total_cards;

random.shuffle(playing_deck)
print(f"\nPlaying with {playing_cards} cards")
#print(playing_deck)

while play_again:
  my_cards = []
  dealer_cards = []

  deal_cards("player",2)
  deal_cards("dealer",2)

  my_score = calculate_card(my_cards)
  dealer_score = calculate_card(dealer_cards)
  print(f"My cards {my_cards}")
  print(f"My Score {my_score}\n")
  print(f"Dealer cards [{dealer_cards[0]}]\n")
  #print(f"Dealer Score {dealer_score}\n")
  #print(playing_deck)

  while not end_of_game:
    extra_card = input("Do you want an extra card? y/n: ")
    if extra_card == 'y':
      deal_cards("player",1)
      calculate_card(my_cards)
      if calculate_card(dealer_cards) < 17:
        deal_cards("dealer",1)
      
      my_score = calculate_card(my_cards)
      dealer_score = calculate_card(dealer_cards)
      print(f"My cards {my_cards}")
      print(f"My Score {my_score}\n")
      print(f"Dealer cards {dealer_cards[0]}\n")
      #print(f"Dealer Score {dealer_score}")
      if my_score > 21:
        end_of_game = True
        print("GAME OVER!")
        print(f"My cards {my_cards}")
        print(f"My Score {my_score}")
        print(f"Dealer cards {dealer_cards}")
        print(f"Dealer Score {dealer_score}")
    else:
      end_of_game = True
      

      if my_score < 21 and dealer_score>21:
        print("You win!")
      elif my_score>dealer_score:
        print("You win!")
      elif my_score == dealer_score:
        print("It's a draw")
      else:
        print("You lose! :(")
      end_of_game = True;
      print(f"My cards {my_cards}")
      print(f"My Score {my_score}")
      print(f"Dealer cards {dealer_cards}")
      print(f"Dealer Score {dealer_score}")

    
    
  if input("Have another? y/n") =="n":
      print("Goodbye, See  you soon")
      play_again=False
      end_of_game = True;
  else:
      play_again=True
      end_of_game = False;
      playing_cards = len(playing_deck)
      #if the deck has less than 10 cards reshuffle
      if playing_cards <= 10:
        playing_deck=[]
        for _ in range(n_decks*4):
          playing_deck += cards
          playing_cards += total_cards
      random.shuffle(playing_deck)
      playing_cards = len(playing_deck)
      clear()
      print(f"\n\nPlaying with {playing_cards} cards")
      #print(playing_deck)
      

  