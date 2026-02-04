"""Given:
person = {"name": "Alice", "age": 30, "city": "Nairobi"}
Print each key."""

import sys


def main():
    person = {"name": "Alice", "age": 30, "city": "Nairobi"}

    #print each key
    for key in person:
        print(key)
    return 0

if __name__ == "__main__":
    sys.exit(main())
