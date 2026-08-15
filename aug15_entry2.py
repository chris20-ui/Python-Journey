gold = 3000

quantity = 0

price = 500

quest = 100

print(f"Current Gold: {gold}")

quantity = int(input("How many potions would you like to buy? "))

gold -= price*quantity



quantity = int(input("How quest have you completed: "))


gold += quest* quantity


print(f"Remaining Gold: {gold}")
