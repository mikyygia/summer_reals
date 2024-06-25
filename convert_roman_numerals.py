"""
    Takes in a roman numeral input and outputs its number equivalent
    
    Rules:
    1. The same roman numeral cannot be repeated more than 3 times in a row
    - V, L, D cannot be repeated at all
    2. I cannot be placed before L, C, D, or M
    3. X cannot be placed before D, M
        etc.
    4. Roman numerals are written from largest to smallest from left to right
    - A smaller numeral placed before a larger numeral indicates subtraction.
    - A smaller numeral placed after a larger numeral indicates addition.
"""


def is_invalid_bef(roman):
    # Confirm rule 2

    watch = roman[0]
    i_watch = ["L", "C", "D", "M"]
    v_watch = ["X", "L", "C", "D", "M"]
    x_watch = ["D", "M"]
    l_watch = ["C", "M"]
    d_watch = ["M"]

    for i in reversed(range(len(roman))):
        for j in range(i + 1):
            if (roman[j] == "I") and (roman[i] in i_watch):
                raise ValueError
            elif (roman[j] == "X") and (roman[i] in x_watch):
                raise ValueError
            elif (roman[j] == "V") and (roman[i] in v_watch):
                raise ValueError
            elif (roman[j] == "L") and (roman[i] in l_watch):
                raise ValueError
            elif (roman[j] == "D") and (roman[i] in d_watch):
                raise ValueError


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

    if ((roman.count("V") >= 2) or (roman.count("L") >= 2) or (roman.count("D") >= 2)):
        raise ValueError

    for i in range(len(roman)):
        if not (roman[i] in counter):
            raise ValueError

        if (i == 0):
            counter[roman[i]] += 1
        else:
            if (roman[i] == roman[i - 1]):
                counter[roman[i]] += 1

                if (counter[roman[i]] > 3):
                    # determine whether or not counter is above 3
                    raise ValueError
            elif (roman[i] != roman[i - 1]):
                # resets counter
                counter = {k: 0 for k in counter}
                counter[roman[i]] += 1


def roman_to_num(roman):
    num = 0

    roman = roman.upper()

    for _ in roman:
        if "IV" in roman:
            num += 4
            roman = roman.replace("IV", "")
        elif "IX" in roman:
            num += 9
            roman = roman.replace("IX", "")
        elif "XL" in roman:
            num += 40
            roman = roman.replace("XL", "")
        elif "XC" in roman:
            num += 90
            roman = roman.replace("XC", "")
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
            raise ValueError

    return num


def main():
    print()

    roman = input("Roman Numeral: ").upper()

    try:
        is_invalid_rep(roman)
        is_invalid_bef(roman)

        print(">>", roman_to_num(roman))

    except ValueError:
        print("Invalid Format")
    except IndexError:
        print("Invalid Format")


if __name__ == "__main__":
    main()
