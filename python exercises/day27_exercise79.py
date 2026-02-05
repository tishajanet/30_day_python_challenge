"""Define a function greet(name) that prints:
Hello, <name>
Call it with a user-provided name."""
import sys


def main():
    def greet(name):
        print(f"hello, {name}")
    greet("Tisha")
    return 0

if __name__ == "__main__":
    sys.exit(main())
