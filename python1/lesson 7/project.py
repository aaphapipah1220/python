i = 0
total = 0
numbers = []

print("Please input a number to be calculated and press enter. If you are done")
print("please write 'Done' and press the enter key. Thank you!")

i = input("Please input a number: ")

while i != "Done":
    if i.isalpha():
        print("Input is invalid")
    elif i.isdigit():
        print("Your input is valid and have beed added to the array")
        numbers.append(i)
        print("Currently the numbers that have been added is as follow: ")
        print(numbers)

    i = input("Please input a number: ")

for number in numbers:
    total = int(total) + int(number)

print("Thank you")