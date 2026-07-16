import bcrypt

username = input ("Username: ")

password = input ("Password: ")


hashed_password = bcrypt.hashpw(
    password.encode("utf-8"),
    bcrypt.gensalt()
)

print("\n Account Successful Created ")


print("Username: ",username)

print("Password: ",hashed_password)