"""Ask the user for two integers a and b.
If both are positive, print "Both positive".
Otherwise, print "At least one is not positive".
"""
import sys


def main():

    #ask the user for two integers
    #tested with values 2 and -1
    try:
        a = int(input("Enter a number: "))
        b = int(input("Enter another number: "))
    except ValueError:
        print("invalid input, please enter a number")
        return 1

    #check if both numbers are positive
    if a > 0 and b > 0:
        print("Both positive")
    else:
        print("At least one is not positive")

    return 0

if __name__ == "__main__":
    sys.exit(main())
