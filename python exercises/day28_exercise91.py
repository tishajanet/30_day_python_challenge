"""Define grade_label(score) that returns "Pass" or "Fail"."""
import sys


def main():
    def grade_label(score):
        if score >= 50:
            return "Pass"
        else:
            return "Fail"

    grade = int(input("Enter your grade: "))
    print(grade_label(grade))

    return 0

if __name__ == "__main__":
    sys.exit(main())
