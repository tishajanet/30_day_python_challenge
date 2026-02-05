"""Ask the user for five numbers.
As each number is entered, print the current maximum so far."""
import sys


def main():
    current_maximum = None

    for number in range(5):
        #check if the user enters a number
      try:
        #ask the user for a number
        number = int(input("Enter a number: "))
      except ValueError:
        print("That's not a number!")
        return 1

      if current_maximum is None or number > current_maximum:
        current_maximum = number
      print("The current maximum number is ", current_maximum)

    return 0

if __name__ == "__main__":
    sys.exit(main())
