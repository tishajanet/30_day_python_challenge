"""Use the return value of one
 function as the argument to another."""
import sys


def main():
    #define a function
    def person():
        return "Tisha"
    def first_name(name):
        print(name)

#use the return value for person() as the argument for first_name
    first_name(person())
    return 0

if __name__ == "__main__":
    sys.exit(main())
