'''
Cash to Coins Exercise

Create a function called calc_dollars. In the function body, define a dictionary and store it in a variable named piggyBank. The dictionary should have the following keys defined.
1. quarters
2. nickels
3. dimes
4. pennies
Once you have given yourself a large stash of coins in your piggybank, look at each key and perform the appropriate math on the integer value to determine how much money you have in dollars. Store that value in a variable named dollarAmount and print it.

'''


# The function should look at each key (pennies, nickels, dimes and quarters) and perform the appropriate math on the integer value to determine how much money you have in dollars. Store that value in a variable named `dollarAmount` and print it
def calc_dollars(**coins):
    total = 0
    for key, value in coins.items():
        if key == 'pennies':
            penny_total = value / 100
        elif key == 'nickels':
            nickel_total = value / 20
        elif key == 'dimes':
            dime_total = value / 10
        elif key == 'quarter':
            quarter_total = value / 4


calc_dollars(pennies=342, nickels=9, dimes=32, quarters=4)

dollarAmount = 8.69
piggyBank = {
    "pennies": 0,
    "nickels": 0,
    "dimes": 0,
    "quarters": 0
}


def sort_coins(money):
    while True:
        if money > .25:
            quarters = (money // .25)
            money = money - (quarters * .25)
            money = round(money, 2)
            piggyBank["quarters"] = quarters
        elif money > .10:
            dimes = (money // .10)
            money = money - (dimes * .10)
            piggyBank["dimes"] = dimes
        elif money > .05:
            nickels = (money // .05)
            money = money - (nickels * .05)
            money = round(money, 2)
            piggyBank["nickels"] = nickels
        elif money > .01:
            pennies = (money // .01)
            money = money - (pennies * .01)
            piggyBank["pennies"] = pennies
            break


sort_coins(dollarAmount)
