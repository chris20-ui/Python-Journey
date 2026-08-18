gold =2000

price = 500
 
bonus = 200

quantity = 0


print(f"Current Gold {gold}")

quantity = int(input("How many swords would you like to buy? "))


if quantity >=4:

 gold -= price * quantity

 gold += bonus* quantity


print(f"Remaining gold: {gold}")