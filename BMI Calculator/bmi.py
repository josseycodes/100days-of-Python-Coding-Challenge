def calculate_bmi(weight, height):
    """
    Calculate BMI (Body Mass Index) using weight in kilograms and height in meters.
    Formula: BMI = weight (kg) / (height (m) * height (m))
    """
    return weight / (height * height)

def categorize_bmi(bmi):
    """
    Categorize BMI into different weight status categories according to WHO standards.
    """
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 24.9:
        return "Normal weight"
    elif bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("Welcome to the BMI Calculator!")
    print("Please enter your weight (in kilograms):")
    weight = float(input())
    print("Please enter your height (in meters):")
    height = float(input())

    bmi = calculate_bmi(weight, height)
    print("Your BMI is: {:.2f}".format(bmi))
    category = categorize_bmi(bmi)
    print("Your weight status is:", category)

    # Provide additional health recommendations
    if category == "Underweight":
        print("You may need to gain weight to improve your health.")
    elif category == "Normal weight":
        print("You have a healthy weight. Keep up the good work!")
    elif category == "Overweight":
        print("Consider losing weight to improve your health.")
    else:
        print("You are in the obese category. It's important to manage your weight for better health.")

if __name__ == "__main__":
    main()
