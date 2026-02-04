"""Using the same list from Exercise 56,
 compute and print the total sum.
Given:
numbers = [10, 20, 30, 40]
Use a for loop to print each number on a new line."""
import sys


def main():
    numbers = [10, 20, 30, 40]

    #create a for loop to print each number on a new line
    for n in numbers:
        print(n)

    #compute the total sum
    total = sum(numbers)
    print(f'Total sum: {total}')

    return 0

if __name__ == "__main__":
    sys.exit(main())
