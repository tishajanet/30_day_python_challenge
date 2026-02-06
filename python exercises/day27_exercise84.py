"""Define a function describe_person(name, age)
that:
prints a sentence
returns the age next year"""
import sys


def main():
    #define a function describe_person
    def describe_person(name, age):
        print(f'{name} is {age} years old.')
        #compute the age next year
        age_next_year = age + 1
        return age_next_year

    #ask the user for their name and age
    #test value name, Sarah age 20
    name = input("What is your name?:")

    #check whether the user entered a number
    try:
        age = int(input("How old are you?:"))
    except ValueError:
        print("Please enter a number.")
        return 1

    #call the function
    next_year = describe_person(name, age)
    #print the returned value
    print(f"{name} will be {next_year} years old next year.")

    return 0

if __name__ == "__main__":
    sys.exit(main())
