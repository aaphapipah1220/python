# import random
import random

# create variable
answer = random.randrange(1, 15)

# introduction
print("Welcome! ")
print("This is an infinite \"Gues The Number\" game.")
print("Try to guess the random number with these hints: ")

# conditional statements
if answer <= 5:
    print("The number is less or equal to 5. ")
elif answer > 5 and answer <= 10:
    print("The number is more than 10, but less or equal to 10. ")
elif answer > 10 and answer < 15:
    print("The number is more than 10, but less or equal to 15. ")

# answer from user
inputted_number = input("\n What is the answer? ")

# convert the inputted answer into integer
num = int(inputted_number)

# loop
while True:
    if answer != num:
        inputted_number = input("\n Wrong answer. What is the answer? ")
        num = int(inputted_number)
    else:
        break

# display message
print(f"Congraulation! yes, the right answer is {inputted_number}")