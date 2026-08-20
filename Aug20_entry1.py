gold = 1500

price = 500

quantity = 0 

bonus = 100

print(f"Current Gold: {gold}")


quantity = int(input("Enter the amount of upgrade would you like to do "))

if quantity >=3:

   gold -= price * quantity

   gold += bonus * quantity

print(f"Total {gold}")

