"""Part A


Create a dictionary:
stats = {
    "count": 10,
    "average": 4.5,
    "valid": True
}
Print each value individually using key access.

Part B
Update:
"count" by increasing it by 5 using compound assignment
"valid" to False
Print the final dictionary."""

import sys


def main():
    #create a dictionary
    stats = {
        "count": 10,
        "average": 4.5,
        "valid": True
    }

    print(stats)

    #print each value individually using key access
    print(f"count: {stats["count"]}")
    print(f"average: {stats["average"]}")
    print(f"valid: {stats["valid"]}")

    #update count by increasing it by 5 using compound assignment
    stats["count"] += 5

    #update valid to false
    stats["valid"] = False

    #print the updated dictionary
    print(stats)

    return 0

if __name__ == "__main__":
    sys.exit(main())
