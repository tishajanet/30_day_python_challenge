"""Define is_even(n) that returns True or False.
Use it inside an if statement."""
import sys


def main():
    def is_even(n):
        return n % 2 == 0

    #ask the user to enter a number
    num = int(input("Enter a number: "))

    #check if the number is even
    if is_even(num):
        print("Even")
    else:
        print("Odd")


    return 0

if __name__ == "__main__":
    sys.exit(main())
