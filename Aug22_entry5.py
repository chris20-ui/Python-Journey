gold = 2000

quantity = 0

price = 500

bonus = 100


print(f"Current Gold {gold}")

quantity = int(input("how many upgrades would you like to do? "))


if quantity >=4:
    gold -= price * quantity

    gold += bonus * quantity

print(f"Remaining Gold {gold}")