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

    return result


def roman_to_decimal(user_input):
    validate_roman_input(user_input)

    switched_map = {y: x for x, y in roman_characters_map.items()}

    allowed_literals = list(roman_characters_map.values())
    allowed_literals.reverse()

    result = 0
    tmp_roman = ''
    tmp_dec = 0

    while user_input != '':
        for input_char in user_input:
            tmp_roman += input_char
            if tmp_roman in allowed_literals and tmp_dec < switched_map.get(tmp_roman):
                tmp_dec = switched_map.get(tmp_roman)
            else:
                result += tmp_dec
                user_input = user_input[len(tmp_roman) - 1:]
                tmp_roman = ''
                tmp_dec = 0
                break

    return result


def main():
    args = parse_app_arguments()

    if args.todecimal is False and args.toroman is False:
        print("One of either flags are required: [-dec] [--todecimal] and [-rom] [--toroman]. See more with --help.")
        exit(1)
    elif args.todecimal is True and args.toroman is True:
        print("Both options: [-dec] [--todecimal] and [-rom] [--toroman] are not allowed. Choose one.")
        exit(1)
    elif args.toroman is True:
        result = decimal_to_roman(args.input)
        print(f"{args.input} => {result}")
    elif args.todecimal is True:
        result = roman_to_decimal(args.input)
        print(f"{args.input} => {result}")


# Run program
main()
