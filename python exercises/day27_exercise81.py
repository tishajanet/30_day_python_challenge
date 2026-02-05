"""Inside a function, define a variable x = 10.
Outside the function, try to print x.
Observe and explain what happens (comment)."""
import sys


def main():
    def my_function():
        x = 10

    my_function()
    #print(x) outside the function x is not defined, so it raises name error
    return 0

if __name__ == "__main__":
    sys.exit(main())
