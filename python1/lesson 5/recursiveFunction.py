def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

print("This is a factorial program. it will count the sum of numbers from 1 until the number given")

while True:
    num = input("To stop. input stop. Give number: ")
    if num == "stop":
        break
    else:
        print(f"the sum from 1 to {str(num)} is {str(factorial(int(num)))}")