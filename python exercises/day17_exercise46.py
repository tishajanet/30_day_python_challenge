"""Ask the user for a number.
Create a boolean variable is_even.
If is_even is True, print "Even number", else print "Odd number"."""
import sys


def main():
    #ask the user to enter a number
    #tested with number 2
    try:
        number = int(input("Enter a number: "))
    except ValueError:
        print("invalid input")
        return 1

    #create a boolean variable is_even
    is_even = number % 2 == 0

    #check whether the number is even or not
    if is_even:
        print("Even number")
    else:
        print("Odd number")
    return 0

if __name__ == "__main__":
    sys.exit(main())
