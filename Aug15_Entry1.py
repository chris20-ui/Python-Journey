gold = 1500

quantity = 0

price = 500


print(f"Current {gold}")

quantity = int(input("How many potions would you like to buy? "))

gold -= price *  quantity

print(f"Remaining gold: {gold}")