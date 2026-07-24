import bcrypt

Username = input ("Create Username: ")

Password = input ("Create Password: ")

hashed_Password = bcrypt.hashpw(
    Password.encode("utf-8"),
    bcrypt.gensalt()
)

print("\n Account Crated Successful")

print("Username: ",Username)

print("Password: ",hashed_Password)
