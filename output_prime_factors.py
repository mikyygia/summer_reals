"""
    Enter a number and find all Prime Factors (if there are any) and display them.
"""

from math import sqrt


def user_input():
    try:
        num = int(input(">> "))

        if num <= 0:
            raise IndexError

    except ValueError:
        print("Invalid")
        return
    except IndexError:
        print("Not in range")
        return

    output_factors(num)


def output_factors(num):
    print(">> ", end="")
    for i in range(1, num + 1):
        # Checks if i is a factor of num then determine if prime
        if (num % i == 0) and (check_prime(i)):
            print(i, end=" ")


def check_prime(n):
    if (n == 1):
        return False

    if (n == 2):
        return True

    for i in range(2, n):
        if (n % i == 0):
            return False
        else:
            continue

    return True


def main():
    print("+++ +++ PRIME FACTORS +++ +++")
    print("A prime factor is a natural number not 1, whose factors are 1 and itself.\n")
    user_input()
    print()


if __name__ == "__main__":
    main()
