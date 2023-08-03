# introduction
print("Welcome! this is a divisor calculator")
print("Give us a number and we'll tell you the divisors number.")

# user input
inputted_number = input("Number: ")

# convert inputted number to integer
num = int(inputted_number)

# display message
print(f"\n The divisors of {inputted_number} are: ")

# for loop
for counter in range (1, num+1):
    if num%counter == 0:
        print((counter))

