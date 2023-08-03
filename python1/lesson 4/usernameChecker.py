# instruction
print("Hallo!")
print("This is a username validator. We'll check if your username is qualifying to our standards or not")
print("our username standards:")
print("1. The username characters are more than 5 characters, but no more than 10 characters")
print("2. The username should be all lowcase")

# input username
username = input("Input your username: ")

# conditional statements
if len(username) < 5 or len(username) >= 10:
    print("Username terlalu pendek")
elif not username.islower():
    print("Hurus harus besar")
else:
    print("Your username is qualified")
