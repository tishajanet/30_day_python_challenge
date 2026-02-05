"""Ask the user for five numbers, store them in a list.
Using the sorted() function and a for-construct,
print the numbers in ascending order without
modifying the original list."""
import sys


def main():
    #ask the user for 5 numbers
    numbers = input("Enter five numbers: ").split()
    numbers = list(map(int, numbers))

    #sort the numbers in the list
    sorted_numbers = sorted(numbers)

    #print the numbers in ascending order
    for num in sorted_numbers:
        print(num)

    return 0

if __name__ == "__main__":
    sys.exit(main())
