for i in range(3):
    Temperature=int(input("Enter Today's Temperature: "))
    if Temperature>=45:
        print("it's very hot today")
    elif Temperature>=25:
        print("finally a relaxing weather")
    else:
        print("it's so cold")