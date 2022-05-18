def get_user_input():
    user_input = input("Provide number: \n")
    return user_input


def validate_decimal_input(user_input):
    if not user_input.isdigit():
        print("You passed wrong input. Must be a decimal number. \n")
        exit(1)


def validate_roman_input(user_input):
    for character in user_input:
        contains = character.upper() in allowed_roman_chars
        if not contains:
            print(f"You passed wrong input. Allowed roman characters are: {allowed_roman_chars}. \n")
            exit(1)


allowed_roman_chars = {"I", "V", "X", "L", "C", "D", "M"}


def decimal_to_roman(user_input):
    validate_decimal_input(user_input)


def roman_to_decimal(user_input):
    validate_roman_input(user_input)


def main():
    option = input("Choose option: \n 1 - Decimal to Roman \n 2 - Roman to Decimal \n")
    if option == "1":
        user_input = get_user_input()
        decimal_to_roman(user_input)
    elif option == "2":
        user_input = get_user_input()
        roman_to_decimal(user_input)
    else:
        print("You choose wrong option or passed wrong input. \n")
        exit(1)


# Run program
main()
