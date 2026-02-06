"""Define greet(name, greeting="Hello").
Call it with and without the greeting argument."""
import sys


def main():
    def greet(name, greeting="Hello"):
        print(name, greeting)

    greet("Tisha", greeting="Hello")
    greet("Tisha")

    return 0

if __name__ == "__main__":
    sys.exit(main())
