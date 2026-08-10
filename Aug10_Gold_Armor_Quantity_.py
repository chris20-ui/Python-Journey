Gold = 2000

quantity = 0

armor_price = 200


print(f"Current Gold: {Gold}")

quantity = int(input("Enter the amount you like to order: "))

Gold -= armor_price*quantity

print(f"Total: {Gold}")