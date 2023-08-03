# create variable
counter = 0
result = 0

# introduction
print("Welcome! This is a multiplicative number program")
print("Give us a number and we'll tell you the multiplicative number until 10 number")

# user input
inputted_number = input("Number: ")

# convert inputted number into integer
num = int(inputted_number)

# display message
print(f"\n multiplicative number of {inputted_number} are: ")

# while loop
while counter < 10:
    result = result + num
    print(result)
    counter = counter + 1