"""Given the function below:
import math
def mystery_function(length1: float, length2: float) -> float:
    result = math.sqrt(length1 ** 2 + length2 ** 2)
    return result
predict its output
then run and verify
This is an example of a function with type annotations.
Type annotations are extra declarations that help with
type hints within your code editor.
They are not required but are helpful."""
import sys
import math

def main():

    def mystery_function(length1: float, length2: float) -> float:
        result = math.sqrt(length1 ** 2 + length2 ** 2)
        return result

    print(mystery_function(2,2))
    return 0

if __name__ == "__main__":
    sys.exit(main())
