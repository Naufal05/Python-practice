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

def is_resource_sufficient(order_ingredients):
    """Return true when order can be and flase when the ingredients are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    """returns the total calculated from coins inserted"""
    print("Please insert coins.")
    total = int(input("How many quarters?:")) * 0.25
    total += int(input("How many dimes?:")) * 0.1
    total += int(input("How many nickles?:")) * 0.05
    total += int(input("How many pennies?:")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """Return true if the payment is accepted or return False if the money is insufficient""" 
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change")
        """profit here is at outside"""
        global profit  
        profit += drink_cost
        return True
    else:
        print("Thats not enough money. Money refunded.")
        return False
    
def make_coffee(drink_name, order_ingradients):
    for item in order_ingradients:
        resources[item] -= order_ingradients[item]
    print(f"Here is your {drink_name} 🍵")

profit = 0
is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")      ,
        print(f"fMilk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")

    else:
        drink = MENU[choice]
        print(drink)
        if is_resource_sufficient(drink["ingredients"]):
            paymnet = process_coins()
            if is_transaction_successful(paymnet,  drink["cost"]):
                make_coffee(choice, drink["ingredients"])