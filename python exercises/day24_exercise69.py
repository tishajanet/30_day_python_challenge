"""items = ["apple", "banana", "cherry"]
Using the enumerate() function and for-construct print:
0: apple
1: banana
2: cherry"""
import sys


def main():
    items = ["apple", "banana", "cherry"]
    for index, item in enumerate(items):
        print(f'{index}: {item}')
    return 0

if __name__ == "__main__":
    sys.exit(main())
