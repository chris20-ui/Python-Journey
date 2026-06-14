for i in range(4):
    Grade = float(input("Enter your grade: "))
    if Grade>=94.50:
        print("High Honor Student")
    elif Grade>=91:
        print("Honor Student")
    elif Grade>=60:
        print("Passed")
    else:
        print("Remidial")