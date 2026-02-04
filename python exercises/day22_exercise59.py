"""Using the word in Exercise 58,
count how many characters it has using a loop (do not use len()).
Ask the user for a word.
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

    #check for the number of characters in the word
    length = 0
    for character in word:
        length += 1
    print(f'Length: {length}')

    return 0

if __name__ == "__main__":
    sys.exit(main())
