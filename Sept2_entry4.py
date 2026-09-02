gold = 2000

price = 500

quantity = 0

bonus =100

print(f"Current Gold {gold}")

quantity = int(input("How many healing potion would you like? "))


if quantity >=4:
    gold -= price* quantity
    gold += bonus* quantity

    print(f"Remaining gold: {gold}")