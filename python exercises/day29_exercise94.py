"""Simple Interest Calculator
a) Write a function to compute simple interest
b) Write a function to compute total amount
c) Use both functions to compute interest from user input"""
import sys


def main():
    #define a function that computes simple interest
    def simple_interest(principal, rate, time):
        return principal * rate * time

    #define a function that computes total amount
    def total_amount(principal, interest):
        return principal + interest

    #ask the user for input
    principal = float(input("Enter a principal value: "))
    rate = float(input("Enter a rate in percentage: "))
    time = int(input("Enter a time: "))

    interest = simple_interest(principal, rate, time)
    total_amount = total_amount(principal, interest)

    #print the interest
    print("The interest is: ",interest)
    #print the total amount
    print("The total amount is: ",total_amount)

    return 0

if __name__ == "__main__":
    sys.exit(main())
