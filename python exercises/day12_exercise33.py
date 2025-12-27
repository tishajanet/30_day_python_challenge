"""Add a new key is_student with value False.

Print the dictionary.
"""
import sys


def main():
    # create a dictionary called person
    person = {"name": "Alice", "age": 25, "country": "Kenya"}

    # print the dictionary
    print(person)

    # print the person's name
    print(f"name: {person["name"]}")

    # print the person's age
    print(f"age: {person["age"]}")

    # update the person's age to 26
    person["age"] = 26

    # updated dictionary
    print(person)

    #add new key is_student
    person["is_student"] = False

    print(person)

    return 0

if __name__ == "__main__":
    sys.exit(main())
