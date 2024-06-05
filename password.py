import random
import string

def generate_password(length):
    if length < 5:
        raise ValueError("Password length should be at least 5 to include all character types.")
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation
    password = [
        random.choice(uppercase_letters),
        random.choice(lowercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters
    password += random.choices(all_characters, k=length-3)
    random.shuffle(password)

    return ''.join(password)

password_length = 8

print("Generated password:", generate_password(password_length))