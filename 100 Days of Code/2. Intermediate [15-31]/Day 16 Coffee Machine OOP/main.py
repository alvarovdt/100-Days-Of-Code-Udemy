from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_menu = Menu()
my_coffee_machine = CoffeeMaker()
my_money_maker_machine = MoneyMachine()


my_coffee_machine.report()
my_money_maker_machine.report()

is_on = True

while is_on:
    menu_options = my_menu.get_items()
    user_choice = input(f"What drinks do you want? ({menu_options}) ").lower()

    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        my_coffee_machine.report()
        my_money_maker_machine.report()
    else:
        drink = my_menu.find_drink(user_choice)
        if drink is not None:
            if my_coffee_machine.is_resource_sufficient(drink):
                if my_money_maker_machine.make_payment(drink.cost):
                    my_coffee_machine.make_coffee(drink)

