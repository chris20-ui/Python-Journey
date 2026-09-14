gold = 2000

quantity = 0

price = 500

bonus = 100


print(f"Current gold {gold}")


quantity = int(input("enter how many upgrade would you like to do "))

if quantity >=4:
    gold -= price * quantity
    gold += bonus * quantity

    print(f"Remaining gold {gold}")