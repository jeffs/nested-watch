"""
This module defines a function to return the factorial of a given
integer.  If called as a script, it prints the factorials of all integer
arguments.
"""

from functools import reduce
from operator import mul
from sys import argv


def product(numbers):
    """
    Return the result of multiplying the given numbers together.
    Return 1 if numbers is empty.
    """
    return reduce(mul, numbers, 1)


def factorial(n):
    """
    Return the product of the integers 1 through n.
    n must be a nonnegative integer.
    """
    return product(range(2, n + 1))


if __name__ == '__main__':
    for n in map(int, argv[1:]):
        print(factorial(n))
