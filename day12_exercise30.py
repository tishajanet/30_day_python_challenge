"""Create a dictionary called person with the following fixed data:

name: "Alice"
age: 25
country: "Kenya"
Print the dictionary exactly as Python represents it."""

import sys


def main():
    #create a dictionary called person
    person = {"name": "Alice", "age": 25, "country": "Kenya"}

    #print the dictionary
    print(person)

    return 0

if __name__ == "__main__":
    sys.exit(main())
