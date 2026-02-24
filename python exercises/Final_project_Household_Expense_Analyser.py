"""
You are given a file expenses.txt with:
category,amount
Your task is to write a program that:
a) Reads the file safely
b) Builds a dictionary of category totals
c) Computes overall expenditure
d) Identifies the highest-spending category
e) Prints a clear financial summary
Rules:
Must use at least four functions
No functions longer than ~15 lines
No global state i.e., no variables on the global scope that are referenced from the functions
All logic must be decomposed"""
import sys

#define a function that reads the file
def read_file_safely(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            #skip the header
            return lines[1:]
    except FileNotFoundError:
        print("File not found")
        return []
    except Exception as e:
        print("Error reading the file")
        return []
    #define a function `that builds a dictionary of category totals
def build_category_totals(lines):
    totals = {}
    for line in lines:
        category, amount = line.split(',')
        amount = float(amount)
        totals[category] = totals.get(category, 0) + amount
    return totals

    #define a function that computes overall spending
def total_expenditure(total):
    return sum(total.values())

    #define a function that identifies the highest spending category
def highest_spending_category(totals):
    if not totals:
        return None, 0
    category = max(totals, key=totals.get)
    return category, totals[category]

    #define a function that prints the financial summary
def print_summary(totals, overall, highest_category,highest_amount):
    print("Financial Summary:")
    for category, amount in totals.items():
        print(f'{category} : {amount}')
        print('Total Expenditure: ' , overall)
        print('Highest Spending: ' , highest_category, highest_amount)
def main():
    filename = "expenses.txt"

    lines = read_file_safely(filename)
    if not lines:
        return 1

    totals = build_category_totals(lines)
    overall = total_expenditure(totals)
    highest_category, highest_amount = highest_spending_category(totals)
    print_summary(totals, overall, highest_category, highest_amount)
    return 0

if __name__ == "__main__":
    sys.exit(main())
