def valid_email(email):
    if "@gmail.com" in email:
        return True
    else:
        return False
print(valid_email("chris@gmail.com"))