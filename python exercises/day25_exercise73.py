"""Given:
stock = {"pen": 10, "book": 0, "eraser": 5}
Print only the items that are out of stock."""
import sys


def main():
    stock = {"pen": 10, "book": 0, "eraser": 5}

    #check for the item out of stock
    for key in stock:
        if stock[key] == 0:
            #print the item out of stock
            print("This item is out of stock:", key)
    return 0

if __name__ == "__main__":
    sys.exit(main())
