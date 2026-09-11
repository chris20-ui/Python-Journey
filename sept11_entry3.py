gold = 4000

quantity = 0

price = 500

bonus = 100


print(f"Current Gold: {gold}")

quantity = int(input("Enter how many gold would you like to buy? "))


if quantity >=8:
    gold -= price * quantity
    gold += bonus * quantity

    print(f"Remaining gold: {gold}")

