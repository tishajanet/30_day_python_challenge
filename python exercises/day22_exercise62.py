"""Print:
key -> value
for each entry in the dictionary. For example,
 if the dictionary has the key-value pair "a" and 36 your programme should print out:
a -> 36"""
import sys


def main():
    person = {"name": "Alice", "age": 30, "city": "Nairobi"}

    for key, value in person.items():
        print(f'{key} -> {value}')
    return 0

if __name__ == "__main__":
    sys.exit(main())
