"""Define a function
that takes a list of numbers and returns their total."""
import sys


def main():
    #define a function that takes a list of numbers and returns the total
    def sum_of_numbers(numbers):
        total = 0
        for number in numbers:
            total += number
        return total

    #create an empty list to store the user input
    list_of_numbers = []

    for i in range(4):
        try:
            #ask the user to enter numbers
            num = int(input("Enter a number: "))
        except ValueError:
            print("Invalid input, please eneter a number.")
            return 1
        list_of_numbers.append(num)

    #print the list of numbers
    print(list_of_numbers)

    #call the function and print the total of the numbers
    print("The total is: ",sum_of_numbers(list_of_numbers))

    return 0

if __name__ == "__main__":
    sys.exit(main())
