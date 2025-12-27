"""Part A
Ask the user for:
their name
their age (convert to int)
their city
Store the data in a dictionary called profile.
Print profile.

Part B
Add a new key age_next_year whose value is the user’s age plus one.
Print the updated dictionary."""

import sys


def main():
    #ask the user for their name, age and city
    name = input("What is your name?: ")
    age = int(input("How old are you?: "))
    city = input("What city are you in?: ")

    #store the data in a dictionary
    profile = {"name": name, "age": age, "city": city}

    #print the dictionary
    print(profile)

    #add a new key to the dictionary called age_next_year
    profile["age_next_year"] = age + 1

    #updated dictionary
    print(profile)

    return 0

if __name__ == "__main__":
    sys.exit(main())
