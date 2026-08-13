Gold = 1000

quantity = 0

price = 100

reward = 250 
print(f"Current Gold: {Gold}")

quantity = int(input("how many potions would you like to buy? "))


Gold -= price * quantity

quantity = int(input("How many quest have you completed: "))

Gold += reward * quantity
print(f"Remaining Gold: {Gold}")