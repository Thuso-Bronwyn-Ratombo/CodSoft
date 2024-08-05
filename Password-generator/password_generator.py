import random
import string

def generate_password(length, use_lower, use_upper, use_digits, use_special):
    if length < 1:
        return "Password length must be at least 1."
    
    # Define the character sets to choose from
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
    
    # Initialize the pool of characters based on user choices
    all_characters = ''
    if use_lower:
        all_characters += lower
    if use_upper:
        all_characters += upper
    if use_digits:
        all_characters += digits
    if use_special:
        all_characters += special

    if not all_characters:
        return "You must select at least one character type."

    # Ensure the password contains at least one of each selected character type
    password = []
    if use_lower:
        password.append(random.choice(lower))
    if use_upper:
        password.append(random.choice(upper))
    if use_digits:
        password.append(random.choice(digits))
    if use_special:
        password.append(random.choice(special))
    
    # Generate the remaining password length
    password += random.choices(all_characters, k=length - len(password))
    
    # Shuffle the result to ensure randomness
    random.shuffle(password)
    
    return ''.join(password)

def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        
        use_lower = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
        use_upper = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
        use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
        use_special = input("Include special characters? (y/n): ").strip().lower() == 'y'

        password = generate_password(length, use_lower, use_upper, use_digits, use_special)
        print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
