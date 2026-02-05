"""Print the squares of numbers from 1 to 10 using range()."""
import sys


def main():

    for num in range(1, 11):
        # print the squares of numbers from 1 to 10
        print(num ** 2)
    return 0

if __name__ == "__main__":
    sys.exit(main())
