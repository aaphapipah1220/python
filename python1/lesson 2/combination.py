# Combination merupakan proses penggabungan beberapa elemen menjadi satu

# Asking for input from the users (Height in meters and weight in kg)

height = float(input("input your height in cm: "))
weight = float(input("input your weight in kg: "))

# if the weight and height is not fulfilling the requirements the program will keep on asking for inputs

# while merupakan sebuah pengulangan (looping) selama kondisi terpenuhi / kondisi bernilai true. Jika kondisi sudah bernilai false / sudah tidak dapat terpenuhi pengulangan akan berhenti

while (height < 50 or height > 200) or (weight < 10 or weight > 200):
    print("Please put in valid height and weight")
    height = float(input("input your height in cm: "))
    weight = float(input("input your weight in kg: "))
else:
    bmi = round((height - 100 * 10 / 100) - weight)

    print(f"Your BMI is {bmi}")

    if bmi < 45:
        print("You are underweight")
    elif bmi > 45 and bmi < 65:
        print("You have a normal weight")
    elif bmi > 65 and bmi < 85:
        print("You are slightly overweight")
    elif bmi > 85 and bmi < 105:
        print("You are obese")
    else:
        print("You are clinically obese")