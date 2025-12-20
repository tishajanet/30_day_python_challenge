"""Given "items = [10, 20, 30]",
create an independent copy using slicing and print both lists."""
import sys


def main():
    items = [10, 20, 30]

    #create an independent copy using slicing
    independent_copy = items[:]

    #print items list
    print(f"items: {items}")

    #print the independent copy list
    print(f"independent_copy: {independent_copy}")

    return 0

if __name__ == "__main__":
    sys.exit(main())
