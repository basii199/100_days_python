MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

current_wallet = 0

def generate_report():
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: ${current_wallet}')

def check_resources(order):
    if order not in MENU.keys():
        return False, []

    missing_ingredients = []
    for ingredient, quantity in MENU[order]['ingredients'].items():

        if quantity > resources.get(ingredient):
            missing_ingredients.append(ingredient)

    return len(missing_ingredients) == 0, missing_ingredients

def process_money():
    def validate_input(prompt):
        while True:
            val = input(prompt)
            if val.isdigit():
                return int(val)
            print('Input a valid whole number. ')

    print('Please insert coins.')
    quarters = validate_input('How many quarters? ')
    dimes = validate_input('How many dimes? ')
    nickels = validate_input('How many nickels? ')
    pennies = validate_input('How many pennies? ')

    return round((quarters * .25) + (dimes * .1) + (nickels * .05) + (pennies * .01), 2)


def process_transaction(order, amount):
    global current_wallet
    current_wallet += MENU[order]['cost']

    for ingredient, quantity in MENU[order]['ingredients'].items():
        resources[ingredient] -= quantity

    return amount - MENU[order]['cost']


def process_order(order):
    if order not in MENU.keys():
        print('Invalid response')
        return

    order_available, missing_ingredients = check_resources(order)

    if not order_available:
        missing_ingredients_list = ", ".join(missing_ingredients)
        print(f"Sorry there is not enough {missing_ingredients_list}")
        return

    amount_paid = process_money()

    if amount_paid < MENU[order]['cost']:
        print(f"Sorry that's not enough money. Refunding ${amount_paid}.")
        return

    user_change = process_transaction(order=order, amount=amount_paid)

    if user_change > 0:
        print(f"Here is ${user_change} in change.")

    print(f'Here is your {order}. Enjoy!')


serving = True
while serving:
    user_prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_prompt == 'off':
        serving = False
    elif user_prompt == 'report':
        generate_report()
    else:
        process_order(user_prompt)