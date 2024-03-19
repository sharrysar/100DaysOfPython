from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_on = True
money = 0

while is_on:
    options = menu.get_items()
    order = input(f"What would you like? ({options}): ")

    if order == "off":
        print("Turning off...")
        is_on = False
    elif order == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        item = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(item) and money_machine.make_payment(item.cost):
            coffee_maker.make_coffee(item)
