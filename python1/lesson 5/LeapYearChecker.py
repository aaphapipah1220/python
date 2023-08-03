# function to check if the year is a leap year or not

def leap_year_checker(year):
    if (year%400 != 0 and year%100 != 0 and year%4 != 0) or (year%400 != 0 and year%100 == 0):
        return False
    else:
        return  True

# instruction
print("Welcome everyone!")
print("This is leap year checker program.")

# input year
inputted_year = input("Input the year: ")

# convert inputted year into integer
year = int(inputted_year)

# call the function
result = leap_year_checker(year)

# conditional statement
if result == True:
    print(inputted_year + " is a leap year")
else:
    print(inputted_year + " is not a leap year")