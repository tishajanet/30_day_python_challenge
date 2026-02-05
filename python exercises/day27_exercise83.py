"""Write a function that:
prints a message
returns None
Assign the result to a variable and print it."""
import sys


def main():
    def my_function(message):
        print(message)
        return None

    #ask the user for input
    message = input("Enter a message: ")
    #assign the result to a variable
    result = my_function(message)
    #print the result
    print(result)
    return 0

if __name__ == "__main__":
    sys.exit(main())
