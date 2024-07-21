import string
import random

def password_generater(length, has_letters, has_numbers, has_symbols):
    """
    Generate a random password based on user-defined criteria
    """
    characters = ''
    
    if has_letters:
        characters += string.ascii_letters
    if has_numbers:
        characters += string.digits
    if has_symbols:
        characters += string.punctuation
    
    if not characters:
        print("Error: At least one character type must be selected.")
        return None
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
   
    while True:
        try:
            length = int(input("Enter the length of the desired password: "))
            if length < 1:
                print("Password length must be a positive integer. Try again!")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid password length.")
    
    
    has_letters = input("Include letters (y/n)?: ").lower() == 'y'
    has_numbers = input("Include numbers (y/n)?: ").lower() == 'y'
    has_symbols = input("Include symbols (y/n)?: ").lower() == 'y'
    
   
    password = password_generater(length, has_letters, has_numbers, has_symbols)
    
    if password:
        print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
