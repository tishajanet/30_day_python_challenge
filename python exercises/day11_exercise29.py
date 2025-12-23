"""Ask the user for:
their name (string)
their age (integer)
their country (string)
Store the results in a list 'profile = [name, age, country]'.

Then produce a new list:
'summary = [profile[0].upper(), profile[1] + 5, profile[2].lower()]'.

Finally print both lists with clear labels."""

import sys


def main():
    #ask the user for their name
    name = input("What is your name? ")

    #ask the user for their age
    age = int(input("How old are you? "))

    #ask the user for their country
    country = input("What country are you from? ")

    # tested with name:Mary, age:20, country:Kenya
    #store the results in a list
    profile = [name, age, country]
    print(profile)

    summary = [profile[0].upper(), profile[1] + 5, profile[2].lower()]
    print(summary)
    return 0


if __name__ == "__main__":
    sys.exit(main())
