gold = 900

quantity = 0

price = 100

mission = 200

print(f"Current Gold {gold}")

quantity = int(input("How many uprade would you like to do? "))

gold -= price *quantity

print(f"Gold After Upgrade {gold}")
quantity = int(input("How many quest have you completed?  "))

gold += mission *quantity

print(f"Remaining Gold: {gold}")