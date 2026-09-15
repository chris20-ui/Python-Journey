gold = 4000

quantity = 0

price = 500

bonus = 100


print(f"Gold: {gold}")


quantity = int(input("Enter the amout you like to buy: "))


if quantity >=4:
    gold -= price * quantity

    gold += bonus * quantity


    print(f"Remaining Gold: {gold}") 