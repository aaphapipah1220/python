# imports
import random

# variables
num = random.randrange(1, 100)

# instruction
print("This is a random generator. We have a variable with random value from 1 to 100 inside of it")
print("If the value is less than 50, we'll let you know! ")

# print answer
print("\n The number is: " + str(num))

# conditional statements
if num < 50:
    print("Answer: Yes! The random number is less than 50")
elif num <= 80:
    print("Answer: Oh no, the answer is between 50 and 80")
else:
    print("Answer: No. The random number is greater than 80")