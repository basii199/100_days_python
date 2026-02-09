from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu_list = menu.get_items()

machine_running = True

while machine_running:
    user_input = input(f'What would you like? ({menu_list}): ').lower()

    if user_input == 'off':
        machine_running = False
    elif user_input == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        if user_input not in menu_list:
            print('Invalid input.')
            continue

        drink = menu.find_drink(user_input)

        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)