"""Ask the user for numbers repeatedly (use a list of inputs given upfront, e.g. 5 numbers).
Stop processing when a negative number is encountered.
Print the numbers processed before stopping.
This will require your use of the 'break' keyword."""
import sys


def main():
    numbers = []
    for i in range(5):

        #ask the user for numbers
        num = int(input("Enter a number:"))
        if num < 0:
            #stop if a negative number is encountered
            break
        numbers.append(num)
    print(numbers)
    return 0

if __name__ == "__main__":
    sys.exit(main())
