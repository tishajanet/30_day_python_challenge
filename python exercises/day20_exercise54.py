"""Ask the user for an optional middle name.
If the input is empty, set middle_name = None.
If middle_name is not None, print the full name with middle name.
Else print only first and last name."""
import sys


def main():

    #ask the user for input
    first_name = input("Enter your first name: ")
    middle_name = input("Enter your middle name: ")
    last_name = input("Enter your last name: ")

    #check if the input is empty
    if middle_name == "":
        middle_name = None

    #check if middle name is not none
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
        print(full_name)

    else:
        print(first_name + " " + last_name)

    return 0

if __name__ == "__main__":
    sys.exit(main())
