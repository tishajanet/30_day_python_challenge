"""Mini-Project 2 — CSV-Like Data Scan
Given the attached file scores.txt where each line contains:
name,score
Your program should:
Open the file safely
Iterate over each line
Extract names and scores
Track:
highest score
corresponding name
Print the top scorer
Constraints:
Use split()
Use numeric conversion
Use compound assignment e.g., += or -= or /= (a combination of an assignment with another operator)
No functions"""
import sys


def main():
    highest_score = -1
    top_scorer = ""

    #open the file safely
    with open("scores.txt", "r") as file:
        next(file)
        #iterate over each line
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            #extract names and scores
            name = parts[0]
            score = int(parts[1])

            highest_score = max(highest_score, score)
            if score == highest_score:
                top_scorer = name

    print("The top scorer is", top_scorer , "with a score of", highest_score)
    return 0

if __name__ == "__main__":
    sys.exit(main())
