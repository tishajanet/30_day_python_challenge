"""Ask the user to enter numbers until they enter 0.
Compute and print the total sum."""
import sys


def main():
    #ask the user to enter a number
    number = int(input("Enter a number: "))
    total = 0

    #check the condition
    while number != 0:

        #compute the total sum
        total += number
        number = int(input("Enter a number: "))

    #print the total sum
    print(f'Total sum: {total}')

    return 0

if __name__ == "__main__":
    sys.exit(main())
