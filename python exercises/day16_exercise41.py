"""Ask the user for:
name
birth year (integer)
country
Store them in a dictionary profile.

Then create a new dictionary summary with:
"NAME" → uppercase name
"age_in_2025" → 2025 - birth_year
"country" → lowercase country
Print both dictionaries with labels.
"""

import sys


def main():
    #test values name-Sandra, birth year- 2005, country - Kenya

    #ask the user to enter their name, birthyear and country
    try:
        name = input("What is your name? ")
        birth_year = int(input("What is your birth year? "))
        country = input("What country are you from? ")
    except ValueError:
        print("please enter correct values")
        return 1

    #store the input in a dictionary
    profile = {"name": name, "birth_year": birth_year, "country": country}


    #create a dictionary summary
    dictionary_summary = {"NAME": name.upper(),
                          "age_in_2025": 2025 - birth_year,
                          "country": country.lower()
                          }

    #print the dictionaries
    print(f"Profile: {profile}")
    print(f"Dictionary Summary: {dictionary_summary}")

    return 0

if __name__ == "__main__":
    sys.exit(main())
