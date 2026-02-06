"""Call the same function using
keyword arguments in reversed order."""
import sys


def main():
    def person(name, age):
        print(f"{name} is {age} years old.")

    #call the function using keyword arguments
    person(age=20, name='Simon')
    return 0

if __name__ == "__main__":
    sys.exit(main())
