"""Given:
rates = {
    "USD": 160.0,
    "EUR": 170.0,
    "GBP": 200.0
}
Ask the user for a currency code.
If the code exists in the dictionary, print the rate.
Otherwise, print "Currency not supported"."""
import sys


def main():
    rates = {
        "USD": 160.0,
        "EUR": 170.0,
        "GBP": 200.0
    }

    #ask the user for a currency code
    currency_code = input("Enter currency code: ").upper()

    #check if the input currency_code exists in the dictionary
    if currency_code in rates:
        print(rates[currency_code])
    else:
        print("Currency not supported")
    return 0

if __name__ == "__main__":
    sys.exit(main())
