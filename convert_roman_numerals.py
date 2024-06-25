"""
    Takes in a roman numeral input and outputs its number equivalent    
"""


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

    roman = input("Roman Numeral: ")
    if (roman_to_num(roman) == 0):
        print("Invalid")
    else:
        print(">>", roman_to_num(roman))


if __name__ == "__main__":
    main()
