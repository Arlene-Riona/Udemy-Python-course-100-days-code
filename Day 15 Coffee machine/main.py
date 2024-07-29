# food cost and material requirements to make the drink
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

# current resources the machine has to make any drink
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def listing_resources(dictionary):
    """This function gives the report of all the resources in the machine."""
    for item in dictionary:
        if item != "coffee" and item != "money":
            print(f"{item.title()}: {dictionary[item]}ml")
        elif item == "coffee":
            print(f"{item.title()}: {dictionary[item]}g")
        elif item == "money":
            print(f"{item.title()}: ${dictionary[item]}")
    return


def check_resources(dictionary, current_resources, food_item):
    """This function returns item name or none based on if there is enough items to make the drink."""
    position = dictionary[food_item]["ingredients"]
    for item1 in current_resources:
        for item2 in position:
            if item2.lower() == item1.lower():
                result = (current_resources[item1] - position[item2])
                if result < 0:
                    return item1
    return "none"


def cost_finder(difference, food_item, users_amount, dictionary):
    """This function returns the machine's output based on the difference of cost and user's amount."""
    cost = dictionary[food_item]["cost"]
    money_from_user = users_amount
    if difference == 0:
        return f"Here is your {food_item.lower()} ☕ Enjoy!"
    elif difference > 0:
        return "Sorry that's not enough money. Money refunded."
    else:
        amt_to_return = money_from_user - cost
        return f"Here is ${round(amt_to_return, 2)} in change.\nHere is your {food_item.lower()} ☕ Enjoy!"


def update_cost_and_qty(dictionary, current_resources, food_item):
    """This function updates the resources and cost (profit) in the machine."""
    position1 = dictionary[food_item]["ingredients"]
    position2 = dictionary[food_item]["cost"]
    for item1 in position1:
        for item2 in current_resources:
            if item1.lower() == item2.lower():
                current_resources[item2] -= position1[item1]
    for item in current_resources:
        if item.lower() == "money":
            current_resources[item] += position2
    return


def amount_calculator(food_item, dictionary, a1=0.0, a2=0.0, a3=0.0, a4=0.0):
    """This function returns the total amount and difference between the cost and the user's amount."""
    money_from_user = a1*0.25 + a2*0.10 + a3*0.05 + a4*0.01
    cost = dictionary[food_item]["cost"]
    difference = cost - money_from_user
    return money_from_user, difference


user_input = input("What would you like? (espresso/latte/cappuccino):").lower()
while True:
    while user_input != "off":
        # if user wants the report
        if user_input.strip().lower() == "report":
            listing_resources(resources)
            user_input = input("What would you like? (espresso/latte/cappuccino):").lower()
            break
        # to check if there is enough materials to make the drink
        result = check_resources(MENU, resources, user_input)
        if result != "none":
            print(f"Sorry there is not enough {result.lower()}.")
            user_input = input("What would you like? (espresso/latte/cappuccino):").lower()
            break
        print("Please insert coins")
        quarters = float(input("How many quarters?: "))
        dimes = float(input("How many dimes?: "))
        nickles = float(input("How many nickles?: "))
        pennies = float(input("How many pennies?: "))
        difference_in_amt = amount_calculator(user_input, MENU, quarters, dimes, nickles, pennies)
        print(cost_finder(difference_in_amt[1], user_input, difference_in_amt[0], MENU))
        if difference_in_amt[1] <= 0:
            update_cost_and_qty(MENU, resources, user_input)
        user_input = input("What would you like? (espresso/latte/cappuccino):").lower()
    if user_input == "off":
        break
