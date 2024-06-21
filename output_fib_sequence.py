"""
    Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.
"""


def output_sequence(num):
    prev = 0
    end = 1

    if num == 0:
        print(0)

    print(prev, end, end=" ")
    new_end = prev + end

    while (new_end <= num):
        print(new_end, end=" ")
        prev = end
        end = new_end
        new_end = prev + end


def output_to_sequence(num):
    prev = 0
    end = 1

    if num == 0:
        return
    elif num == 1:
        print(0)

    print(prev, end, end=" ")

    if num == 2:
        return

    for _ in range(2, num):
        new_end = prev + end
        print(new_end, end=" ")
        prev = end
        end = new_end


def get_information():
    try:
        num = int(input("Enter an integer: "))

        if num < 0:
            raise IndexError

        print("1. generate a sequence to integer")
        print("2. generate a sequence of integer length long")
        option = int(input("Option: "))

        if not (1 <= option <= 2):
            raise IndexError

    except ValueError:
        print("Invalid")
    except IndexError:
        print("Not in range")

    output_to_sequence(num) if option == 2 else output_sequence(num)


def main():
    print("+++ +++ FIBONACCI SEQUENCE +++ +++")
    get_information()
    print()


if __name__ == "__main__":
    main()
