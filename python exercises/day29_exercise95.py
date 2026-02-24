"""Loan Repayment Summary
a) Function to compute monthly repayment
b) Function to compute total repayment
c) Print a summary using both"""
import sys

#define a function to compute monthly repayment
def compute_monthly_repayment(principal, rate, time_in_months):
    return principal * (1 + rate) ** time_in_months

#define a function to compute total repayment
def compute_total_repayment(monthly_repayment, time_in_months):
    return monthly_repayment * time_in_months

def main():
    #ask the user for input
    principal = float(input("Enter the amount: "))
    rate = float(input("Enter the rate: "))
    time_in_months = int(input("Enter the number of months: "))

    #call the functions
    monthly_payment = compute_monthly_repayment(principal, rate, time_in_months)
    total_payment = compute_total_repayment(monthly_payment, time_in_months)

    #print the summary
    print("Monthly payment: ", monthly_payment)
    print("Total payment: ", total_payment)

    return 0

if __name__ == "__main__":
    sys.exit(main())
