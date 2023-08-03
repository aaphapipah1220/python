# function to check if the number is odd or even

def odd_even_checker(num):
    if num < 1:
        print("The number is less than 1 : ")
    elif num > 100:
        print("The number is more than 100 : ")
    else:
        if num%2 == 0:
            print("The number is even!")
        else:
            print("The number is odd!")

# instruction
print("Hallo!")
print("I need you to put a number between 1 - 100")

# user input
inputted_number = input("Give me the number: ")

# convert input to integer
num = int(inputted_number)

# call the function to print the result
odd_even_checker(num)
