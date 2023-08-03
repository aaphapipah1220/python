# isalpha berfungsi untuk memeriksa karakter dalam string berbentuk aphabet
# isdigit berfungsi untuk memeriksa karakter dalam string berbentuk digit/number

# variable declaration
i = input("please input a number or a string: ")

# check if input is a string or integer
if i.isalpha(): # check if input is a string
    print("You have inputted a string.")
elif i.isdigit(): # check if input is a integer
    print("You have inputted an integer.")

#closing
print("thank you!")
