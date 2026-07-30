import bcrypt

  
username = input ("Create a Username: ")

password = input ("Create a Password: ")


hashed_password = bcrypt.hashpw(
    password.encode("utf-8"),
    bcrypt.gensalt()
)

print("\n Account has been Created ")


print("Username: ",username)

print("Password: ",hashed_password)