"""Ask the user for an integer.
If the number is greater than 10, print "Large number"."""
import sys


def main():

    #ask the user for an integer
    try:
        number = int(input("Enter an integer: "))
    except ValueError:
        print("Invalid input, please enter an integer")
        return 1

    #check if the number is greater than 10
    if number > 10:
        print("Large number")
    else:
        print("Not a large number")

    return 0

if __name__ == "__main__":
    sys.exit(main())
