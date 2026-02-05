"""Define a function say_hello() that prints "Hello, world!".
Call the function."""
import sys


def main():
    def say_hello():
        print("Hello, world!")
    say_hello()
    return 0

if __name__ == "__main__":
    sys.exit(main())
