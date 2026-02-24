"""Mini-Project 1 — Word Frequency Counter (File-Based)

Using the with-construct to read files
The with-construct is a handy way to open files while ensuring that file will always be closed even if the program is interrupted. If files remain open at the end of a program, this affects the number of files that can be opened on the operating system and it is easy to quickly exhaust the number of possible open files when processing thousands of files. Here is a template on how to responsibly open files in Python:

with open("myfile.txt") as f: # uses the open() built-in and returns the file handle 'f'
    for row in f: # iterate over the file using a for-construct
        print(row) # print each row

Given a text file (e.g. text.txt):
Open the file using with-construct shown below
Iterate over each line
Split lines into words
Build a dictionary counting word occurrences
Print the final dictionary
Constraints:
No custom functions
No libraries
Normalize words to lowercase"""
import sys


def main():
    #open the file using with construct
    with open("text.txt", "r") as f:
        word_counts = {}
        for line in f:
            #normalize lines to lowercase
            line = line.lower()
            #split lines into words
            words = line.split()

        #build dictionary counting word occurrences
        for word in words:
            if word in word_counts:
                word_counts[word] += 1

            else:
                word_counts[word] = 1


    print(word_counts)
    return 0

if __name__ == "__main__":
    sys.exit(main())
