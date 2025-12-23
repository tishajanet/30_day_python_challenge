"""Ask the user to enter four integers.
Store them in 'nums'.
Replace:
the first number with its square.
the last number with its cube.
The compute and print the sum of all four numbers."""
import sys


def main():

#ask the user for four integers
#tested with values 1 2 3 4
    user_input = input("Enter four integers: ")

#convert into a list
    nums = user_input.split()

#check whether exactly four numbers are entered
    if len(nums) != 4:
        print("ENTER ONLY FOUR INTEGERS")
        return 1

#try converting the values in the list to integers
    try:
        nums = list(map(int, nums))
        print(nums)

#return an error if any of the values is not an integer
    except ValueError:
        print("ENTER ONLY INTEGERS")
        return 1

#square of the first number in the list
    nums[0] = nums[0] ** 2
    print(nums[0])

#cube of the last number in the list
    nums[3] = nums[3] ** 3
    print(nums[3])

#print new list with the new values
    print(nums)

#sum of the four numbers
    sum_of_all_four_numbers = sum(nums)
    print(sum_of_all_four_numbers)

    return 0

if __name__ == "__main__":
    sys.exit(main())
