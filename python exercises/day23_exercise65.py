"""Use a while loop to print numbers from 5 to 1 so that your program produces the following output:
5
4
3
2
1
Bonus question: What happens if the suite does not include a statement
that modifies the variable in the assignment expression? Try it!"""
import sys


def main():
    num = 5

    while num >= 1:
        print(num)
        num -= 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
