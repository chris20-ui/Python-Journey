import bcrypt 


username = input ("Create Username: ")

password = input ("Create Password: ")



hashed_password = bcrypt.hashpw(
    password.encode("utf-8"),
    bcrypt.gensalt()
)


print("\n Create Account Successful ")


print(" \n--- Login ---")

login_username = input ("Username: ")
login_password = input ("Password: ")


if login_username == username and bcrypt.checkpw(
    login_password.encode("utf-8"),
    hashed_password
):
    print("Login successful!")
else:
    print("Invalid username or password.")