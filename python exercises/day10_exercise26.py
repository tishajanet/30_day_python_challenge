"""Given "values = [5, 6, 7, 8]", create "first_two"
containing only the first two items using slicing."""
import sys


def main():
    values = [5, 6, 7, 8]

    #slice the list to contain the first two items
    first_two = values [0:2]

    #print the new list
    print(first_two)

    return 0

if __name__ == "__main__":
    sys.exit(main())
