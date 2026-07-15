import bcrypt

username = input ("Enter Username: ")

password = input ("Enter Password: ")

hashed_password = bcrypt.hashpw(
    password.encode("utf-8"),
    bcrypt.gensalt()
)

print("\n Succesful Account Creation ")

print("Username: ",username)

print("Password: ",hashed_password)