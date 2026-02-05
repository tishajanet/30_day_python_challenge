"""Given a list of banned words, check whether any appear in a user-provided message.
Stop checking as soon as one is found.
"""
import sys


def main():
    banned_words = ["stupid", "dumb", "idiot"]

    #ask the user for a message
    message = input("Enter a message: ")

    #check if the message contains a banned word
    for word in banned_words:
        if word in message:
            print("This message contains a banned word:", word)
            break

    return 0

if __name__ == "__main__":
    sys.exit(main())
