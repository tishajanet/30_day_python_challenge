"""Ask the user for:
name
three test scores (integers)
Store the data in a dictionary:
student = {
    "name": ...,
    "scores": [...],
}
Compute the average score and add it to the dictionary.
Then:
If the average is ≥ 70, status is "Pass"
If the average is ≥ 50 and < 70, status is "Supplementary"
Otherwise, status is "Fail"
Add "status" to the dictionary and print the final record neatly.
Constraints:
Must use if / elif / else
Must use and
Must use compound assignment at least once
Must reuse Week 1–3 ideas (lists, dicts, arithmetic)"""
import sys


def main():

    #ask the user for input
    user_name = input("Enter your name: ")
    test_scores = input("Enter your test scores: ")

    #convert the scores to a list of integers
    scores = test_scores.split()
    scores = list(map(int, scores))

    #check if 3 test scores were entered
    if len(scores) != 3:
        print("Test scores should be 3")
        return 1

    #create a dictionary
    student = {"name": user_name,
               "scores": scores}

    #compute the average score
    total = 0
    total += scores[0]
    total += scores[1]
    total += scores[2]
    average_score = total / len(scores)

    #add the average to the dictionary
    student["average_score"] = average_score

    if average_score >= 70:
        student["status"] = "Pass"
    elif average_score >= 50 and average_score < 70:
        student["status"] = "Supplementary"
    else:
        student["status"] = "Fail"

    #print the new dictionary
    print(student)

    #print final record
    #tested with name:Tisha, scores:70,80,90
    print(f'Name: {student["name"]}')
    print(f'Scores: {student["scores"]}')
    print(f'Average score: {student["average_score"]}')
    print(f'Status: {student["status"]}')

    return 0

if __name__ == "__main__":
    sys.exit(main())
