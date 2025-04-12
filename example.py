#!/usr/bin/env python

def fibonacci(n):
    """
    Returns the nth Fibonacci number.

    :param n: The position in the Fibonacci sequence (0-indexed).
    :return: The nth Fibonacci number.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

print(fibonacci(10))  # Output: 55
