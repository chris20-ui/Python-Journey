gold = 4000


price = 500

quantity = 0

bonus = 100

print(f"Current gold: {gold}")


quantity = int(input("Enter how many upgrade would you like to do? "))


if quantity >=4:
    gold -= price * quantity
    gold += bonus * quantity

print(f"Total Gold: {gold}")
