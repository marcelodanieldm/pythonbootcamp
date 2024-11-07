MENU = {

"espresso": {
    ingredients:{
    "water": 50,
    "coffee": 18,
},
    "cost":1.5,
},

"latte": {
    ingredients:{
    "water": 200,
    "milk": 150,
    "coffee": 24,
}, 
"cost": 2.5 ,
}, 

"cappuccino": {
    ingredients:{
    "water": 250,
    "milk": 100,
    "coffee": 24,
}, 
"cost": 1.5 ,
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
    total += int(input("How many quarters?: "))*0.25
    total += int(input("How many dimes?: "))*0.1
    total += int(input("How many nickles?: "))*0.05
    total += int(input("How many pennies?"))*0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """Returns true when the payment is accepted, and false when there is no enough money """
    if money_received >= drink_cost:
        change = round(money_received - drink_cost,2)
        print(f"Here is the ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry there is no enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item]-= order_ingredients[item]
        print("Here is your {drink_name}!")
    
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
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
        if is_transaction_successful(payment, drink["cost"]):
            make_coffee(choice, drink["ingredients"])




