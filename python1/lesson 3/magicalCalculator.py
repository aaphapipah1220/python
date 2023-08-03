# Calculator

# import
from __future__ import division

# variables
num1 = 0
num2 = 0

# opening
print("Hi there everyone! welcome to the magical calculator!")
print("And here, by using the magical calculator, I can tell u all of the answers!")
print("All you need to do.. is to tell me the 2 magic numbers")

# user input
num1 = int(input("Can you tell me what is the first number? "))
num2 = int(input(f"{str(num1)}.. eh? nice number. Now can you tell me the second number? "))

# result
print("hmm.. okayy then.. let me think..")
print("AHA! Here's my answer!")

print(f"{str(num1)} + {str(num2)} = {str(num1 + num2)}")
print(f"{str(num1)} x {str(num2)} = {str(num1 * num2)}")
print(f"{str(num1)} - {str(num2)} = {str(num1 - num2)}")
print(f"{str(num1)} : {str(num2)} = {str(num1 / num2)}")

print("Tadaaa~ that's my answers folks! hope that you enjoyed using the magical calculator")
print("Thank you!")