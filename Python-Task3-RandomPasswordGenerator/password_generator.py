import random
import string


def generate_password(length, use_uppercase, use_lowercase,
                      use_numbers, use_symbols):

    character_sets = []

    if use_uppercase:
        character_sets.append(string.ascii_uppercase)

    if use_lowercase:
        character_sets.append(string.ascii_lowercase)

    if use_numbers:
        character_sets.append(string.digits)

    if use_symbols:
        character_sets.append(string.punctuation)

    all_characters = "".join(character_sets)

    password = []

    # Make sure every selected character type is included
    for characters in character_sets:
        password.append(random.choice(characters))

    # Fill the remaining characters
    while len(password) < length:
        password.append(random.choice(all_characters))

    random.shuffle(password)

    return "".join(password)


print("==========================================")
print("       RANDOM PASSWORD GENERATOR")
print("==========================================")

while True:

    try:
        length = int(input("\nEnter password length (minimum 8): "))

        if length < 8:
            print("Error: Password must be at least 8 characters long.")
            continue

    except ValueError:
        print("Error: Please enter a valid number.")
        continue

    print("\nChoose the character types to include.")
    print("At least two types must be selected.")

    uppercase = input("Include uppercase letters? (y/n): ").lower() == "y"
    lowercase = input("Include lowercase letters? (y/n): ").lower() == "y"
    numbers = input("Include numbers? (y/n): ").lower() == "y"
    symbols = input("Include symbols? (y/n): ").lower() == "y"

    selected_types = sum([
        uppercase,
        lowercase,
        numbers,
        symbols
    ])

    if selected_types < 2:
        print("Error: Please select at least two character types.")
        continue

    password = generate_password(
        length,
        uppercase,
        lowercase,
        numbers,
        symbols
    )

    print("\n------------------------------------------")
    print("Generated Password:", password)
    print("------------------------------------------")

    again = input("\nGenerate another password? (yes/no): ").lower()

    if again not in ("yes", "y"):
        print("\nThank you for using the Password Generator!")
        break