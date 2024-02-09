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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def costs():
    print("Please insert coins.")
    quarter = int(input("How many quarters? : "))
    dime = int(input("How many dimes? : "))
    nickel = int(input("How many nickels? : "))
    pennie = int(input("How many pennies? : "))
    summ = round(0.01 * pennie + 0.05 * nickel + 0.1 * dime + 0.25 * quarter, 2)
    return summ


def resource(coffee):
    resources["water"] -= MENU[coffee]["ingredients"]["water"]
    resources["milk"] -= MENU[coffee]["ingredients"]["milk"]
    resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]
    if resources["water"] < 0:
        print("Sorry there is not enough water.")
        return False
    elif resources["milk"] < 0:
        print("Sorry there is not enough milk.")
        return False
    elif resources["coffee"] < 0:
        print("Sorry there is not enough coffee.")
        return False
    else:
        return True


def resource_again(coffee):
    resources["water"] += MENU[coffee]["ingredients"]["water"]
    resources["milk"] += MENU[coffee]["ingredients"]["milk"]
    resources["coffee"] += MENU[coffee]["ingredients"]["coffee"]


end = True


while end:
    coffee_type = input("What would you like? (espresso, latte, cappuccino): ")
    if coffee_type == "report":
        print(resources)
    elif coffee_type == "espresso":
        if resource(coffee_type):
            cost = MENU["espresso"]["cost"]
            summa = costs()
            change = round(summa - cost, 2)
            if change >= 0:
                print(f"Here is ${change} in change")
                print("Here is your espresso. Enjoy!")
            else:
                print("Sorry")
                resource_again(coffee_type)
        else:
            end = False
    elif coffee_type == "latte":
        if resource(coffee_type):
            cost = MENU["latte"]["cost"]
            summa = costs()
            change = summa - cost
            if change >= 0:
                print(f"Here is ${change} in change")
                print("Here is your latte. Enjoy!")
            else:
                print("Sorry")
                resource_again(coffee_type)
        else:
            end = False
    elif coffee_type == "cappuccino":
        if resource(coffee_type):
            cost = MENU["cappuccino"]["cost"]
            summa = costs()
            change = summa - cost
            if change >= 0:
                print(f"Here is ${change} in change")
                print("Here is your cappuccino. Enjoy!")
            else:
                print("Sorry")
                resource_again(coffee_type)
        else:
            end = False
