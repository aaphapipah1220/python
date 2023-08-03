# importing the random library
from welcome import welcome
import random

# Declare and assign variable
operator = random.randrange(1, 3)
num1 = random.randrange(1, 100)
num2 = random.randrange(1, 100)
result = 0
operator_sign = ""
answer = 0

# conditional statements + results
if operator == 1:
    result = num1 + num2
    operator_sign = "+"
elif operator == 2:
    result = num1 - num2
    operator_sign = "-"
else:
    result = num1 * num2
    operator_sign = "*"

# introduction text
print(welcome)

# show questions
print(f"What is {num1} {operator_sign} {num2} ?")

# forever loop
# the game will keep on asking the player to answer until the player give the correct answer

while answer != result:
    temp = input("Answer: ")

    answer = int(temp)
    if answer == result:
        break
    else:
        print("\n Wrong answer. Please try again")

# correct answer
print("\n congratulation! your answer is correct")