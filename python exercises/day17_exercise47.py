"""Ask the user for a number.
Print:
"Negative" if the number is less than 0
"Zero" if the number is 0
"Positive" otherwise"""

import sys


def main():

    #ask the user to enter a number
    #tested with values -1, 0, 1
    try:
        number = int(input("Enter a number: "))
    except ValueError:
        print("invalid input, please enter a number")
        return 1

    #check whether the number meets certain conditions
    if number < 0:
        print("Negative")
    elif number == 0:
        print("Zero")
    else:
        print("Positive")

    return 0

if __name__ == "__main__":
    sys.exit(main())
