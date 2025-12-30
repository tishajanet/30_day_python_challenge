"""Ask the user for:
a username
a boolean flag "is_admin" (True/False)
Given:
access_level = 1
If the user is "admin" or is_admin is True, increase access_level by 4.
Otherwise, increase it by 1.
Print the final access level."""
import sys


def main():
    access_level = 1

    #ask the user for a username
    #tested with username jane
    username = input("Enter your username: ")

    #ask the user for a boolean flag
    #tested with true
    admin_input = input("Are you are an admin? ").strip().lower()

    #check whether the user entered true or false
    if admin_input != "true" and admin_input != "false":
        print("invalid input, please enter true or false")
        return 1

    #convert the input into boolean
    is_admin = admin_input == "true"

    if username == "admin" or is_admin:
        access_level = access_level + 4
    else:
        access_level = access_level + 1

    #print the final access level
    print(f"ACCESS_LEVEL: {access_level}")

    return 0

if __name__ == "__main__":
    sys.exit(main())
