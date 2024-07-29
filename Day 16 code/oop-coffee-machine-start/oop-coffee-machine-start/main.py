from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def menu_maker(user_input, MENU):
    # MenuItem class is given the object menu_list
    menu_list = MenuItem(user_input, MENU[user_input]["ingredients"]["water"], MENU[user_input]["ingredients"]["milk"], MENU[user_input]["ingredients"]["coffee"], MENU[user_input]["cost"])
    return menu_list

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

# classes are given an object
food_menu = Menu()
coffee_menu = CoffeeMaker()
money_menu = MoneyMachine()

while True:
    while True:
        user_input = input("What would you like? (espresso/latte/cappuccino):").lower()
        if user_input == "report" or user_input == "off":
            # if user wants the report
            if user_input == "report":
                coffee_menu.report()
                money_menu.report()
                break
            # if user wants to switch off the machine
            if user_input == "off":
                break
        else:
            result = menu_maker(user_input, MENU)
            # returns T/F if the drink is possible to be made
            status_for_making_drink = coffee_menu.is_resource_sufficient(result)
            # returns T/F based on the amount of money available to make the drink
            payment_status = money_menu.make_payment(result.cost)
            if payment_status:
                coffee_menu.make_coffee(result)
    if user_input == "off":
        break