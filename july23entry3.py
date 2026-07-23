import bcrypt

username = input ("Create Username: ")

password = input ("Create Password: ")

hashed_Password = bcrypt.hashpw(
    password.encode("utf-8"),
    bcrypt.gensalt()
)

print ("\n Account Successful Creaeted ")

print ("Username: ",username)

print("Password: ",hashed_Password)