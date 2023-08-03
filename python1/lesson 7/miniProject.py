#number and array declaration
i = 0
total = 0
numbers = []

# pembukaan dan pembuatan input
print("Please input a number to be calculated and press enter. If you are done")
# print("please write 'Done' and press the enter key. Thank you!")

i = input("Please input a number: ")

# loop & check
while i != "Done":
    if i.isalpha(): #cek if input is a string
        print("Input is invalid")
    elif i.isdigit(): #cek if input is a digit
        print("Your input is valid and have been added is as follow ")
        print(numbers) #showing the array

# ===================================================

    i = input("Please input a number: ")
    # # Loop to add each number inside the array
for number in numbers:
    total = int(total) + int(number)

    # # closing
print("Thank you for using the advance calculator!")
print(f"The total of your number is... {str(total)} Hope you enjoyed making it! ")
