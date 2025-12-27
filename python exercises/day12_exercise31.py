"""Using the dictionary from the previous exercise, print:

the person’s name
the person’s age"""

import sys


def main():
    # create a dictionary called person
    person = {"name": "Alice", "age": 25, "country": "Kenya"}

    # print the dictionary
    print(person)

    #print the person's name
    print(f"name: {person["name"]}")

    #print the person's age
    print(f"age: {person["age"]}")

    return 0

if __name__ == "__main__":
    sys.exit(main())
