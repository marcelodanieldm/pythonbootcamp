MENU :{

resources = {

    "water": 300,
    "milk": 200,
    "coffee": 100,
}


resources = {

    "water": 300,
    "milk": 200,
    "coffee": 100,
}


resources = {

    "water": 300,
    "milk": 200,
    "coffee": 100,
}
}

profit = 0
resources = {

    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resources_sufficient(order_ingredients):
    """Returns when the order can be made, or there is no ingredients"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"There is not enough {item}.")
            return False
    return True

def process_coins():
    """Returns the total calculated from coins inserted"""
    print("Insert coin ")
    total = int(input("How many quarters?: "))*0.25
    total = int(input("How many dimes?: "))*0.1
    total = int(input("How many nickles?: "))*0.05
    total = int(input("How many pennies?"))*0.01

    return total



        


is_on = True


while is_on:
    choice = input("What would you like? espresso/latte/cappuccino ")
    
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Coffee: {resources['coffee']} gr")
        print(f"Milk: {resources ['milk']} ml")
        print(f"Water: {resources ['water']} ml ")
        print(f"Money: ${profit}.-")
    else:
        if is_resources_sufficient(drink[ingredients])



