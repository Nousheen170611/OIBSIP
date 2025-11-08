import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    characters = ""
    
    if use_letters:
        characters += string.ascii_letters   # a-z, A-Z
    if use_numbers:
        characters += string.digits          # 0-9
    if use_symbols:
        characters += string.punctuation     # !@#$%^&*() etc.

    # Handle empty character set
    if not characters:
        print("❌ No character types selected! Please select at least one.")
        return None

    # Generate password using random choices
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


# Main program
print("🔐 RANDOM PASSWORD GENERATOR 🔐")

# User input validation
try:
    length = int(input("Enter password length (e.g., 8–20): "))
    if length < 4 or length > 50:
        print("⚠️ Please enter a length between 4 and 50.")
    else:
        use_letters = input("Include letters? (y/n): ").lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        password = generate_password(length, use_letters, use_numbers, use_symbols)
        if password:
            print("\n✅ Your random password is:", password)

except ValueError:
    print("❌ Invalid input! Please enter a valid number for password length.")
