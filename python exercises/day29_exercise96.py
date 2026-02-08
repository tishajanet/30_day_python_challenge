"""Grade Analysis
a) Function to compute average score
b) Function to assign grade label
c) Apply both to a list of scores"""
import sys


def main():
    #define a function to compute average score
    def average_score(grades):
     average = sum(grades) / len(grades)
     return average

    #define a function to assign grade label
    def grade_label(average):
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        else:
            return "D"

    #create an empty list
    scores = []

    #ask the user for input
    for i in range (4):
        num = int(input("Enter your grade: "))
        scores.append(num)

    print("List of scores: ", scores)
    print("Average score is: ", average_score(scores))
    print("Grade label: ", grade_label(average_score(scores)))


    return 0

if __name__ == "__main__":
    sys.exit(main())
