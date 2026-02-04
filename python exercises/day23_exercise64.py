"""Given a list of integers, print only the positive numbers.
This will require the use of the 'continue' keyword."""
import sys


def main():
    integers = [1, -8, 5, 6, -4]

    for num in integers:
        #check if the numbers in the list are positive numbers
        if num <= 0:
            continue
        #print the positive numbers
        print(num)
    return 0

if __name__ == "__main__":
    sys.exit(main())
