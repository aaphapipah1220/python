# infinite loop merupakan perulangan yang tidak memiliki kondisi berhenti / selalu true

# introduction
print("Hello! Aku ")
print("Do you want to play with me? (type the answer with y for yes or n for no)")

# user input
answer = input("y / n ? ")

# infinite loop
while True:
    if answer != "y":
        print("\n I'm giving you another chance. Do you want to play with me? ")
        answer = input(" y / n ? ")
    else:
        break

# display message
print("\n Yes! Let's play and learn together about Python ")