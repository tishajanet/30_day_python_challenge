"""Ask the user for their age.
If the age is at least 18, print "Adult".
Otherwise, print "Minor"."""
import sys


def main():
    #ask the user to enter their age
    try:
        age = int(input("Enter your age: "))
    except ValueError:
        print("Please enter a number.")
        return 1

    #check whether the age is at least 18
    if age >= 18:
        print("Adult")
    else:
        print("Minor")

    return 0

if __name__ == "__main__":
    sys.exit(main())
