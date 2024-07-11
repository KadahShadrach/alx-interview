#!/usr/bin/python3
"""
Minimum operations
"""

def minOperations(n: int) -> int:
    """ Minimum Operations needed to get n S characters """
    next = 'S'
    body = 'S'
    op = 0
    while (len(body) < n):
        if n % len(body) == 0:
            op += 2
            next = body
            body += body

        else:

            op += 1
            body += next
        if len(body)  !=n:
            return 0
        return op
