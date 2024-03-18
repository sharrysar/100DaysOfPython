# Digital Coffee Machine
def resource_check(ingredients, resources):
    for ingredient, amount in ingredients.items():
        if resources[ingredient] < amount:
            return ingredient

def process_payment(cost, payment):
    if payment < cost:
        return 1
    elif payment > cost:
        change = round(payment - cost, 2)
        return change
    elif payment == cost:
        return 0
    
def make_order(ingredients, resources):
    for ingredient, amount in ingredients.items():
        updated_ingredient = resources[ingredient] - amount
        resources[ingredient] = updated_ingredient
    return resources

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

cost = {
    "espresso": 1.5,
    "latte": 2.5,
    "cappucino": 3.0
}

money = 0
ongoing = True

while ongoing:
    order = input("What would you like? (espresso, latte, cappuccino): ")

    if order == "off":
        break
    elif order == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    else:
        check = resource_check(MENU[order]['ingredients'],resources)
        if check == 'milk' or check == 'coffee' or check == 'water':
            print(f"Sorry, there is not enough {check}")
            break
        quarters = float(input("Please insert coins.\nHow many quarters?: "))
        dimes = float(input("How many dimes?: "))
        nickels = float(input("How many nickels?: "))
        pennies = float(input("How many pennies?: "))
        payment = sum([quarters*.25, dimes*.10, nickels*.05, pennies*.01])
        payment_check = process_payment(cost[order], payment)
        if payment_check == 0:
            resources = make_order(MENU[order]['ingredients'], resources)
            money += cost[order]
            print(f"Here is ${payment_check} in change. Enjoy your {order}!")
        elif payment_check == 1:
            print("Sorry, that's not enough money. Money refunded.")
            ongoing = False
        else:
            resources = make_order(MENU[order]['ingredients'], resources)
            money += cost[order]
            print(f"Here is ${payment_check} in change. Enjoy your {order}!")
