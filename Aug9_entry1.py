Material = 1000
quantity= 0
price = 550


print(f" Current Materials: {Material}")

quantity = int(input("How many do you want to buy? "))

Material -= price *quantity

print(f"Remaining Materials: {Material}")