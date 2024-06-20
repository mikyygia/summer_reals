"""
    Enter a number and have the program generate PI up to that many decimal places.
"""
from mpmath import mp


def pi_output(num):
    mp.dps = num + 1
    print(mp.quad(lambda x: mp.exp(-x**2), [-mp.inf, mp.inf]) ** 2)
    return


def main():
    print("+++ +++ GENERATE DIGITS OF PI +++ +++")
    try:
        integer = int(input(">> "))

        if ((integer < 0) or (integer > 170)):
            raise IndexError

        pi_output(integer)
    except ValueError:
        print("INVALID: Integer only")
    except IndexError:
        print("Not in range")


if __name__ == "__main__":
    main()
