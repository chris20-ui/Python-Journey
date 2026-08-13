Gold = 1200

quantity = 0


price = 300


print(f"Current Gold: {Gold}")

quantity = int(input("How many potions would you like to buy? "))

Gold -= price*quantity


print(f"Remaining Gold: {Gold}")