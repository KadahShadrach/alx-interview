#!/usr/bin/python3
"""
Minimum operations
"""

def minOperations(n: int) -> int:
    """ Minimum Operations needed to get n S characters """
    if n < 2:
        return 0

    next_copy = 'S'
    body = 'S'
    operations = 0

    while len(body) < n:
        if n % len(body) == 0:
            # If the length of body is a divisor of n, we do a Copy All and a Paste
            next_copy = body
            operations += 2  # One for Copy All, one for Paste
            body += body  # Doubling the body
        else:
            # If not, we only do a Paste operation
            body += next_copy
            operations += 1

    return operations
