import bcrypt

username = input ("Create Username: ")
password = input ("Create Password  ")


hashed_password = bcrypt.hashpw(
    password.encode("utf-8"),
    bcrypt.gensalt()
)


print("\n Account Created ")


print("USERNAME: ",username)
print("PASSWORD: ",hashed_password)