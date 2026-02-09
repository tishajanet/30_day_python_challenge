"""Transaction Totals
a) Function to sum transaction values
b) Function to apply tax
c) Produce final total"""
import sys


def main():
    #define a function that sums transaction values
    def transaction_total(transactions):
        total = sum(transactions)
        return total

    #define a function to apply tax
    def tax(amount, rate):
        return amount * rate / 100

    #ask the user to enter the tax rate
    try:
        rate = float(input("Enter the rate in percentage: "))
    except ValueError:
        print("Please enter a valid number for tax rate.")
        return 1

    #ask the user to enter their transactions
    transactions = []
    for i in range (4):
        try:
            num = int(input("Enter a value: "))
            transactions.append(num)
        except ValueError:
            print('Please enter a number!')
            return 1


    total = transaction_total(transactions)
    tax_amount = tax(total, rate)
    final_total = total + tax_amount

    #the test values are 1000, 2000, 3000, 4000
    print("The transactions are: ", transactions)
    print("The total is: ", total)
    print("The tax is: ", tax_amount)
    print("The final total is: ", final_total)



    return 0

if __name__ == "__main__":
    sys.exit(main())
