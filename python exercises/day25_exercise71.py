"""Given a list of test scores:
compute the average
count how many are ≥ 50
compute the average for those that are ≥ 50
Print both results."""

import sys


def main():
    test_scores = [80, 70, 40, 90,80]

    #compute the average of the test scores
    average_of_test_scores = sum(test_scores) / len(test_scores)
    print("The average score is:", average_of_test_scores)
    scores_above_fifty = []

    #set condition for test scores above 50
    for score in test_scores:
        if score >= 50:
            print("This score is greater than 50: ", score)
            scores_above_fifty.append(score)

    #compute the average for scores above 50
    average_passed = sum(scores_above_fifty) / len(scores_above_fifty)
    print("The average score is:", average_passed)

    return 0

if __name__ == "__main__":
    sys.exit(main())
