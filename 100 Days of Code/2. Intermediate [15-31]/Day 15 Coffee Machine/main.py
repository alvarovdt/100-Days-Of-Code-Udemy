from data import MENU
from data import resources

my_money = 0.0
machine_money = 0.0

machine_on = True
def ask_and_insert_coins():
  local_money = 0.0
  print("Please insert coins")
  quarters = int(input("How many quarters? (25cents)"))*0.25
  dimes    = int(input("How many dimes? (10cents)"))*0.10
  nickels  = int(input("How many nickles? (5cents)"))*0.05
  pennies  = int(input("How many pennies? (1cent)"))*0.01
  local_money = pennies + nickels + dimes + quarters
  return local_money

def check_available_ressources(type_of_drink):
  if type_of_drink == 'espresso':
    if resources['water'] > MENU['espresso']['ingredients']['water'] and resources['coffee'] > MENU['espresso']['ingredients']['coffee']:
      print("OK")
      return True
    else: 
      print("KO")
      return False
  else:
    if resources['water'] > MENU[type_of_drink]['ingredients']['water'] and resources['coffee'] > MENU[type_of_drink]['ingredients']['coffee'] and resources['milk'] > MENU[type_of_drink]['ingredients']['milk']:
      return True
    else:
      return False
def check_money(mmoney, drink_price):
  if mmoney >= drink_price:
    return True
  else: 
    return False

while machine_on == True:
  option = input("What would you like? (espresso/latte/cappuccino): ").lower()


  if option == "off":
    print("Turning off the coffee machine")
    machine_on = False
  elif option == "report":
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${machine_money}")
  else:
    if check_available_ressources(option):
        my_money = ask_and_insert_coins() 
        if check_money(my_money, MENU[option]["cost"]):
          resources['water'] -= MENU[option]['ingredients']['water']
          resources['coffee'] -= MENU[option]['ingredients']['coffee']
          if option != 'espresso':
            resources['milk'] -= MENU[option]['ingredients']['milk']
          machine_money += MENU[option]['cost']
          my_money -=MENU[option]['cost']
        else:
          print("Error, not enough money")
    else:
        print("Error, not enough ressources")
    
    
    print(f"Machine money = {machine_money} returned money: {my_money}")
    my_money=0