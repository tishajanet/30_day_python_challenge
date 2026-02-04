"""Ask the user for a word.
Print each character on a separate line."""
import sys


def main():

    #ask the user for a word
    word = input('Enter a word: ').strip()

    #check if the user entered valid input
    if not word:
        print("You did not enter a word.")
        return 1

    if not word.isalpha():
        print("Invalid input.")
        return 1

    #print each character on a separate line
    #tested with the word hey
    for character in word:
        print(character)

    return 0

if __name__ == "__main__":
    sys.exit(main())
