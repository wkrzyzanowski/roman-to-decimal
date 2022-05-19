import argparse

roman_characters_map = {
    1: "I",
    2: "II",
    3: "III",
    4: "IV",
    5: "V",
    6: "VI",
    7: "VII",
    8: "VIII",
    9: "IX",
    10: "X",
    40: "XL",
    50: "L",
    90: "XC",
    100: "C",
    400: "CD",
    500: "D",
    900: "CM",
    1000: "M"
}


def parse_app_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-dec', '--todecimal', help='Tells program that conversion will be between ROMAN and DECIMAL',
                        action='store_true')
    parser.add_argument('-rom', '--toroman', help='Tells program that conversion will be between DECIMAL and ROMAN',
                        action='store_true')
    parser.add_argument('-i', '--input',
                        help="Program input number. When flag is set to [--toroman] DECIMAL input should be provided, "
                             "otherwise [--todecimal] ROMAN format is required.")
    args = parser.parse_args()
    return args


def validate_decimal_input(user_input):
    if not user_input.isdigit():
        print("You passed wrong input. Must be a decimal number. \n")
        exit(1)


def validate_roman_input(user_input):
    for character in user_input:
        contains = character.upper() in list(roman_characters_map.values())
        if not contains:
            print(f"You passed wrong input. Allowed roman characters are: {list(roman_characters_map.values())}. \n")
            exit(1)
