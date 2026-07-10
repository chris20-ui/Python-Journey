for i in range(4):

    Grade = float (input("Enter your Grade: "))

    if Grade>=99:
        print("Achiever")

    elif Grade>=80:
        print("Great")

    elif Grade>=60:
        print("You Passed")

    else:
        print("Remedial")