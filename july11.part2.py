for i in range(4):

    Grade = float(input ("Enter Grade: "))

    if Grade >=99:
        print("Outstanding")
    

    elif Grade >=90:
        print("Honor Student")


    elif Grade >= 60:
        print("Passed")

    else:
        print("Fail")