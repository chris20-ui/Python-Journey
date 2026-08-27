gold = 4000

price = 500


quantity = 0

bonus = 100


print(f"Current GOld: {gold}")


quantity = int(input("Enter how many potions would you like to buy? "))

if quantity >=4:
    gold -= price * quantity

    gold += bonus * quantity

    print(f"Remaining Gold: {gold}")