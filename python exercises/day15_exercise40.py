"""settings = {"volume": 5}
Overwrite "volume" with 10 and print the dictionary."""
import sys


def main():
    settings = {"volume": 5}

    #overwrite volume with 10
    settings["volume"] = 10

    #print the dictionary
    print(settings)
    return 0

if __name__ == "__main__":
    sys.exit(main())
