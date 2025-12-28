"""data = {"a": 1, "b": 2, "c": 3}
Print the number of key–value pairs"""
import sys


def main():

    data = {"a": 1, "b": 2, "c": 3}
    key_value_pairs = len(data)

    #print the number of key value pairs
    print(key_value_pairs)

    return 0

if __name__ == "__main__":
    sys.exit(main())
