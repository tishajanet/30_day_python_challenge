"""Part A
Ask the user for:
student name
three test scores (integers)
Store the scores in a list.

Part B
Create a dictionary called student with keys:
"name" → student name
"scores" → list of scores
Print the dictionary.

Part C
Compute the average score and add a new key:
"average" → average score (float)
Print the final dictionary."""

import sys


def main():

    #part A
    try:
        #ask the student for their name and test scores
        student_name = input("Enter your name: ")
        test_scores = input("Enter three test scores: ")

        #store the values of test scores into a list
        test_scores = test_scores.split()

        #convert the values in the list into integers
        test_scores = list(map(int, test_scores))

        #check whether the values in the list are three
        if len(test_scores) != 3:
            print("Please enter three scores.")
            return 1

    except ValueError:
        print("Please enter valid integer test scores.")
        return 1

    #part B

    #create a dictionary called student
    student = {"name" : student_name,
            "scores" : test_scores
            }

    #print the dictionary
    print(student)

    #part C

    #compute the average of the test scores
    total_sum = sum(test_scores)
    average_score = total_sum / len(test_scores)
    print("The average score is:", average_score)

    #add a new key called average to the dictionary
    student["average"] = average_score

    #print the final dictionary
    print(student)

    return 0

if __name__ == "__main__":
    sys.exit(main())
