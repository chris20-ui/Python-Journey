import bcrypt

username = input("Create a username:")

password = input("Create a password:")

hashed_password=bcrypt.hashpw(
password.encode("utf-8"),
bcrypt.gensalt()
)

print("\n Account Successfully Created! ")

print("Username: ",username)
print("Password; ",hashed_password)
