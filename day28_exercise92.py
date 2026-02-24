"""Use the return value of one
 function as the argument to another."""
import sys
#define a function that returns a name
def person():
    return "Tisha"
#define a function that takes the name and prints it
def first_name(name):
    print(name)

def main():
#use the return value for person() as the argument for first_name
    first_name(person())
    return 0

if __name__ == "__main__":
    sys.exit(main())
