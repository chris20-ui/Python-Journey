gold = 2000
quantity = 0
price= 500
bonus = 100


print(f"Current Price {gold} ")

quantity = int(input("Enter how mant times would you like to upgrade? "))


if quantity >=4:
    gold -= price * quantity
    gold += bonus * quantity

    print(f"Remaining balance {gold}")