print("===================================")
print("          BMI CALCULATOR")
print("===================================")

while True:
    try:
        weight = float(input("Enter your weight (kg): "))
        height = float(input("Enter your height (m): "))

        if weight <= 0 or height <= 0:
            print("Error: Weight and height must be greater than 0.\n")
            continue

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        print("\n-----------------------------------")
        print(f"BMI: {bmi:.2f}")
        print(f"Category: {category}")
        print("-----------------------------------")

        choice = input("\nDo you want to calculate again? (yes/no): ").lower()

        if choice not in ("yes", "y"):
            print("\nThank you for using the BMI Calculator!")
            break

    except ValueError:
        print("Error: Please enter numbers only.\n")