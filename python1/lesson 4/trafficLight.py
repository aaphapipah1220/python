# instruction
print("Hallo")
print("I need you to type the color of traffic light (red or yellow or green")

# user input
color = input("Give me the color: ")

# conditional statement
if color == "red":
    print("It's red! stop and wait for a few minutes")
elif color == "yellow":
    print("It's yellow! Be carefully, friends!")
elif color == "green":
    print("It's green! Go go go")
# else:
#     print("There's no color like that in traffic light")

input_color = input("give me the color again? ")

while True:
    if color != input_color:
        input_color = input("try again.. ")
    else:
        break

print("Thank you")