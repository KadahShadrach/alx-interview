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
            next_copy = body
            operations += 2
            body += body
        else:
            body += next_copy
            operations += 1

    return operations
