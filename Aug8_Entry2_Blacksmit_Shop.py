Gold = 1000

swords_price = 200

sword = 0

print(f"Current Gold: {Gold}")


sword= int(input("How many swords did you buy? "))

Gold -= swords_price  * sword

print(f"Remaining Gold: {Gold}")