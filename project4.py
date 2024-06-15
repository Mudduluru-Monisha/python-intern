import random
import string

def generate_password(length):
    # Define the character sets to choose from
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    # Ensure the password has at least one character from each set
    all_characters = lower + upper + digits + special
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]

    # Fill the rest of the password length with random choices from all characters
    password += random.choices(all_characters, k=length-4)
    
    # Shuffle the list to ensure the order is random
    random.shuffle(password)
    
    # Join the list into a string and return
    return ''.join(password)

def main():
    # Provide user instructions
    print("Welcome to the Password Generator!")
    print("This tool generates strong, secure passwords.")
    
    # Get user input for password length and number of passwords
    try:
        length = int(input("Enter the desired password length (minimum 12 characters): "))
        if length < 12:
            print("Password length should be at least 12 characters.\nPlease try again.")
            return
        num_passwords = int(input("Enter the number of passwords to generate: "))
        if num_passwords < 1:
            print("Number of passwords should be at least 1.")
            return
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return
    
    # Generate and display the passwords
    print("\nGenerated Passwords:")
    for _ in range(num_passwords):
        print(generate_password(length))

if __name__ == "__main__":
    main()
