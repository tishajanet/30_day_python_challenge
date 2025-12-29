"""colors = ["red", "green", "blue"]
Ask the user for a color.
If the color is in the list, print "Color available",
else print "Color not found"""
import sys


def main():
    colors = ["red", "green", "blue"]

    #ask the user for a color
    color_choice = input("Enter a color: ").lower()

    #check if the user entered the correct input
    if color_choice.isdigit():
        print("INVALID INPUT")
        return 1

    #check if the colour is in the list or not
    if color_choice in colors:
        print("Color available")
    else:
        print("Color not found")

    return 0

if __name__ == "__main__":
    sys.exit(main())
