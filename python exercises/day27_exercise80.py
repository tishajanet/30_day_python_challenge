"""define a function double_number(n) that:
assigns n * 2 to a local variable
prints the result
Call it with a number from input."""
import sys


def main():
    def double_number(n):
        result = n * 2
        print(result)

    #ask the user for a number
    number = int(input("Enter a number: "))

    #call the function with a number from input
    double_number(number)
    return 0

if __name__ == "__main__":
    sys.exit(main())
