gold = 2000

quantity = 0

price = 500


bonus = 100


print(f"Current Gold: {gold}")

quantity = int(input("How many potion would you like to buy? "))

if quantity >=4:
  gold -= price * quantity
  gold += bonus * quantity


  print(f"Remaining Gold: {gold}")