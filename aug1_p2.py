positive = 0
negative = 0
zero     = 0
for i in range(5):

    number  = int(input("Enter a number "))

    if number >0:
        positive+=1

    elif number <0:
        negative+=1

    else:
        zero+=1

        print(f"Positive: {positive}")

        print(f"Negative: {negative}")

        print(f"Zero: {zero}")