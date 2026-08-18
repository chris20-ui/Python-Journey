wallet = 20000

quantity = 0

price = 200

sideline = 60


print(f"Current Money: {wallet}")

quantity = int(input("How ticket for spider meow would you like to buy? "))

wallet -= quantity * price


print(f"Remaning Money: {wallet}")

quantity = int(input("How many client avail today ? "))

wallet += sideline *quantity

print(f" Amount of Money: {wallet}")



