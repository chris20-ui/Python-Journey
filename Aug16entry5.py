Gold = 5000

quantity = 0

price = 200

quest  = 150

print(f"Current Gold: {Gold}")

quantity = int(input(" how many potions would you like to buy? "))


Gold += price *quantity


quantity = int(input("How many quest have you completed? "))

Gold -= quest * quantity


print(f"Remaining Gold: {Gold}")