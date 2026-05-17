def valid_email(email):
    if ("@gmail.com") in email:
        return True
    else:
        return False
    
user_input = input("Enter your Email: ")

print(valid_email(user_input))