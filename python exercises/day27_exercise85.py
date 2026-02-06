"""Call the same function with three different inputs."""
import sys


def main():
    def double_number(n):
        return n * 2

    #call the function with three different inputs
    print(double_number(2))
    print(double_number(3))
    print(double_number(4))

    return 0

if __name__ == "__main__":
    sys.exit(main())
