gold = 2000

price  = 500


quantity = 0

quest =200


print(f"current wallet: {gold}")


quantity = int (input("How many upgrade would you like to do? "))

if quantity>=4:
  gold -= price * quantity

  gold += quest * quantity

print(f"Remaining gold: {gold}")