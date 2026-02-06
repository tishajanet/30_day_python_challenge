"""Define add(a, b) that returns their sum.
Call it using positional arguments."""
import sys


def main():
    def add(a, b):
        return a + b
    #call the function using positional arguments
    add(2, 2)
    print(add(2,2))
    return 0

if __name__ == "__main__":
    sys.exit(main())
