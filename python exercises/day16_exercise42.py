"""grades = {
    "A": 80,
    "B": 70,
    "C": 60,
    "D": 50
}
Ask the user for a grade letter (A, B, C, or D).
Print the corresponding minimum score."""
import sys


def main():
    grades = {
        "A": 80,
        "B": 70,
        "C": 60,
        "D": 50
    }

    #ask the user for a grade letter
    grade_letter = input("Enter a grade letter: ").upper()

    #check if the grade letter exists in the dictionary
    if grade_letter in grades:
        print("The minimum score is", grades[grade_letter])
    else:
        print("Invalid grade letter, please enter A,B,C or D")
    return 0

if __name__ == "__main__":
    sys.exit(main())
