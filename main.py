from app_utils import *


def decimal_to_roman(user_input):
    validate_decimal_input(user_input)

    allowed_numerals = list(roman_characters_map.keys())
    allowed_numerals.reverse()  # Sort values from high to low
    user_input_number = int(user_input)

    result = ''

    while user_input_number != 0:
        for numeral in allowed_numerals:
            if user_input_number >= numeral:
                user_input_number = user_input_number - numeral
                result += str(roman_characters_map.get(numeral))
                break

    print(f"{user_input} => {result}")


def roman_to_decimal(user_input):
    validate_roman_input(user_input)


def main():
    args = parse_app_arguments()

    if args.todecimal is False and args.toroman is False:
        print("One of either flags are required: [-dec] [--todecimal] and [-rom] [--toroman]. See more with --help.")
        exit(1)
    elif args.todecimal is True and args.toroman is True:
        print("Both options: [-dec] [--todecimal] and [-rom] [--toroman] are not allowed. Choose one.")
        exit(1)
    elif args.toroman is True:
        decimal_to_roman(args.input)
    elif args.todecimal is True:
        roman_to_decimal(args.input)


# Run program
main()
