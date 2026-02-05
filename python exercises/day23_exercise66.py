"""Ask the user repeatedly for input until they enter "quit".
Print each input except "quit"."""
import sys


def main():

    #ask the user for input
    #tested with word hello
    word = input("Enter a word: ")

    #check the condition
    while word != 'quit':
        print(word)
    #ask the user for input repeatedly
        word = input("Enter a word: ")
    return 0

if __name__ == "__main__":
    sys.exit(main())
