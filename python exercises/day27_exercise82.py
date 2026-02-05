"""Rewrite double_number(n) so it returns the result instead of printing it.
Print the returned value outside the function."""
import sys


def main():
    def double_number(n):
        result = n * 2
        return result

    #ask the user for input
    number = int(input("Enter a number: "))
    #call the function
    result = double_number(number)
    #print the returned value outside the function
    print(result)
    return 0

if __name__ == "__main__":
    sys.exit(main())
