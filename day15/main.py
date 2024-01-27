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
    "money": 0,
}
end = False


def latte():
    resources["water"] = MENU["latte"]["ingredients"]["water"]
    resources["milk"] = MENU["latte"]["ingredients"]["milk"]
    resources["coffee"] = MENU["latte"]["ingredients"]["coffee"]
    print("Your Latte is ready , Enjoy ☕")


def espresso():
    resources["water"] = MENU["espresso"]["ingredients"]["water"]
    resources["milk"] = MENU["espresso"]["ingredients"]["milk"]
    resources["coffee"] = MENU["espresso"]["ingredients"]["coffee"]
    print("Your Cappuccino is ready , Enjoy ☕")


def cappuccino():
    resources["water"] = MENU["cappuccino"]["ingredients"]["water"]
    resources["milk"] = MENU["cappuccino"]["ingredients"]["milk"]
    resources["coffee"] = MENU["cappuccino"]["ingredients"]["coffee"]
    print("Your Cappuccino is ready , Enjoy ☕")


def check_resources(resource, coffee):
    if MENU[coffee]["ingredients"]["water"] > resource["water"]:
        return 1
    elif MENU[coffee]["ingredients"]["coffee"] > resource["coffee"]:
        return 1
    elif MENU[coffee]["ingredients"]["milk"] > resource["milk"]:
        return 1
    else:
        return 0


def calc_money(coffee):
    print("Insert coins")
    quarter = int(input("Enter quarters"))
    dime = int(input("Enter dime"))
    nickle = int(input("Enter nickle"))
    penny = int(input("Enter pennies"))

    money = quarter * 0.25 + 0.1 * dime + 0.05 * nickle + 0.01 * penny

    if money < MENU[coffee]["cost"]:
        return -1

    else:
        return money % MENU[coffee]["cost"]


def print_report():
    """Prints the remaining resources left in the machine"""
    print(f"""Water: {resources["water"]}
Milk: {resources["milk"]}
Coffee: {resources["coffee"]}
Money: {resources["money"]}""")


def coffee_machine():
    x = input("What would you like to have(espresso/latte/cappuccino)\n").lower()
    if x == "report":
        print_report()
    elif x == "latte":
        y = calc_money(x)
        z = check_resources(resources, x)
        if y >= 0 and z == 0:
            latte()
            print(f"Your change is {y}")
            resources["money"] += MENU[x]["cost"]
        if y == -1:
            print("Insufficient funds")
        if z == 1:
            print("Insufficient resources")
        return False

    elif x == "espresso":
        y = calc_money(x)
        z = check_resources(resources, x)
        if y >= 0 and z == 0:
            espresso()
            print(f"Your change is {y}")
            resources["money"] += MENU[x]["cost"]
        if y == -1:
            print("Insufficient funds")
        if z == 1:
            print("Insufficient resources")
        return False

    elif x == "cappuccino":
        y = calc_money(x)
        z = check_resources(resources, x)
        if y >= 0 and z == 0:
            cappuccino()
            print(f"Your change is {y}")
            resources["money"] += MENU[x]["cost"]
        if y == -1:
            print("Insufficient funds")
        if z == 1:
            print("Insufficient resources")
        return False
    else:
        return True


while not end:
    end = coffee_machine()
