# BMI Calculator Program

def calculate_bmi(weight, height):
    """Calculate BMI using formula: BMI = weight / (height * height)"""
    return weight / (height ** 2)

def classify_bmi(bmi):
    """Return category based on BMI value"""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def get_valid_input(prompt, min_val, max_val):
    """Get valid numeric input within range"""
    while True:
        try:
            value = float(input(prompt))
            if value < min_val or value > max_val:
                print(f"⚠️ Please enter a value between {min_val} and {max_val}.")
                continue
            return value
        except ValueError:
            print("❌ Invalid input! Please enter a numeric value.")

def main():
    print("=== 🧮 BMI CALCULATOR ===")

    # Get user inputs with validation
    weight = get_valid_input("Enter your weight (in kilograms): ", 10, 300)
    height = get_valid_input("Enter your height (in meters): ", 0.5, 2.5)

    # Calculate BMI
    bmi = calculate_bmi(weight, height)

    # Classify BMI
    category = classify_bmi(bmi)

    # Display result
    print("\n=== RESULT ===")
    print(f"Your BMI: {bmi:.2f}")
    print(f"Category: {category}")

if __name__ == "__main__":
    main()
