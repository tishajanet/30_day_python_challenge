"""Ask the user for a value using input().
If the input is empty, print "No input provided".
Else if the input is numeric, print "Numeric input".
Else print "Text input".
Constraints:
No loops
No exception handling
Use:
.isdigit()
truthiness of strings
if / elif / else"""

import sys


def main():

    #ask the user for input
    #texted with no input and values 1 and "hello"
    value = input("Enter a value: ")

    #check if the input is empty
    if not value:
        print("No input provided")

    #check if the input is numeric
    elif value.isdigit():
        print("Numeric input")

    #check if the input is a text
    else:
        print("Text input")

    return 0

if __name__ == "__main__":
    sys.exit(main())
