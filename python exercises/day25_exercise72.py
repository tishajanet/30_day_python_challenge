"""Ask the user for a sentence.
Print only the words longer than 4 characters."""
import sys


def main():
    #ask the user for a sentence
    sentence = input("Enter a sentence: ")
    words = sentence.split()

    #condition to check for words longer than 4 characters
    for word in words:
        if len(word) > 4:
            print(word)
    return 0

if __name__ == "__main__":
    sys.exit(main())
