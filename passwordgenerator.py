import random
import string

def generate_intelligent_password(length=12):
    # Define the characters to use for generating the password
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Ensure that the password length is reasonable
    if length < 8:
        length = 8

    # Create a password with a mix of characters
    password = {
        random.choice(uppercase_letters) +
        random.choice(lowercase_letters) +
        random.choice(digits) +
        random.choice(special_characters) +
        ''.join(random.choice(uppercase_letters + lowercase_letters + digits + special_characters) for _ in range(length - 4))
    }

    # Shuffle the characters to make it random
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

if __name__ == "__main__":
    password_length = int(input("Enter the desired password length: "))
    password = generate_intelligent_password(password_length)
    print("Intelligent Password:", password)


