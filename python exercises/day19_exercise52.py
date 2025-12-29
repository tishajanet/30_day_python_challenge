"""Ask the user for a list of three words (build a list manually).
If the list is non-empty, print "List has items".
Else print "Empty list"."""
import sys


def main():
    #create an empty list to store the items
    words = []

    #add items to the list
    #tested with values hey, hello, hi
    words.append(input("Enter the first word: "))
    words.append(input("Enter the second word: "))
    words.append(input("Enter the third word: "))

    #print the list
    print(words)

    #check if the list is non-empty
    if words:
        print("List has items")
    else:
        print("Empty list")

    return 0

if __name__ == "__main__":
    sys.exit(main())
