"""
    Takes in a roman numeral input and outputs its number equivalent
    
    Rules:
    1. The same roman numeral cannot be repeated more than 3 times in a row
    - V, L, D cannot be repeated at all
    2. I cannot be placed before L, C, D, or M
    3. X cannot be placed before D, M
    4. Roman numerals are written from largest to smallest from left to right
    - A smaller numeral placed before a larger numeral indicates subtraction.
    - A smaller numeral placed after a larger numeral indicates addition.
"""


def is_invalid_rep(roman):
    # Confirm rule 1

    if len(roman) == 1:
        return

    counter = {
        "I": 0,
        "V": 0,
        "X": 0,
        "L": 0,
        "C": 0,
        "D": 0,
        "M": 0,
    }

    more_than_once = ["V", "L", "D"]

    for i in range(len(roman)):
        if (i == 0):
            counter[roman[i]] += 1
        else:
            if (roman[i] == roman[i - 1]) and (roman[i] in more_than_once):
                raise ValueError
            elif (roman[i] == roman[i - 1]):
                counter[roman[i]] += 1

                if (counter[roman[i]] > 3):
                    # determine whether or not counter is above 3
                    raise ValueError
            elif (roman[i] != roman[i - 1]):
                # resets counter
                counter = {k: 0 for k in counter}


def roman_to_num(roman):
    num = 0

    roman = roman.upper()

    if "IV" in roman:
        num += 4
        roman = roman.replace("IV", "")
    elif "IX" in roman:
        num += 9
        roman = roman.replace("IX", "")
    elif "XL" in roman:
        num += 40
        roman = roman.replace("XL", "")
    elif "CD" in roman:
        num += 400
        roman = roman.replace("CD", "")
    elif "CM" in roman:
        num += 900
        roman = roman.replace("CM", "")

    for i in roman:
        if (i == "I"):
            num += 1
        elif (i == "V"):
            num += 5
        elif (i == "X"):
            num += 10
        elif (i == "L"):
            num += 50
        elif (i == "C"):
            num += 100
        elif (i == "D"):
            num += 500
        elif (i == "M"):
            num += 1000
        else:
            return 0

    return num


def main():
    print()

    roman = input("Roman Numeral: ").upper()

    try:
        is_invalid_rep(roman)

        print(">>", roman_to_num(roman))

    except ValueError:
        print("Invalid")


if __name__ == "__main__":
    main()
