import string
import random

# Define the character sets to use for password generation
upper_letters = string.ascii_uppercase
lower_letters = string.ascii_lowercase
digits = string.digits
symbols = string.punctuation

# Combine the character sets into a single string for easy use in password generation
all_chars = upper_letters + lower_letters + digits + symbols

def generate_password(length):
    """Generates a random password of the specified length."""
    password_chars = random.choices(all_chars, k=length)
    password = "".join(password_chars)
    return password

# Generate an example password and print it to the console
password = generate_password(8)
print(f"Generated password: {password}")

# Pause the script to prevent it from exiting immediately
input("Press Enter to exit...")
