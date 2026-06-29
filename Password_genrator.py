import random
import string

print("=" * 40)
print("     PASSWORD GENERATOR")
print("=" * 40)

letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

all_characters = letters + numbers + symbols

try:
    length = int(input("\nEnter password length: "))

    if length <= 0:
        print("Password length must be greater than 0")

    else:
        password = ""

        for i in range(length):
            password += random.choice(all_characters)

        print(f"\nGenerated Password: {password}")

except ValueError:
    print("Please enter a valid number.")