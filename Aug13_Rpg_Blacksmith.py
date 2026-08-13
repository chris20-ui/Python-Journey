gold = 2000

quantity = 0

cost = 100

reward = 50

print(f"Current Gold {gold}")

quantity = int(input("How many sword would you like to buy? "))

gold -= cost * quantity


quantity = int(input("Enter how many quest have you completed: "))


gold += reward * quantity

print(f"Total Gold:   {gold}")