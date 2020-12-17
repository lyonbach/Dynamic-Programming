"""
Python implementation of the second chapter code.
Original videos can be viewed from the following link:
https://www.youtube.com/watch?v=oBt53YbR9Kk
"""

def grid_traveller(m, n,):

    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    return grid_traveller(m - 1, n) + grid_traveller(m, n - 1)


def grid_traveller_memo(m: int, n: int, memo: dict={}):

    value = memo.get((m, n))
    if not value:
        if m == 1 and n == 1:
            value = 1
        elif m == 0 or n == 0:
            value = 0
        else:
            value = grid_traveller_memo(m - 1, n, memo) + grid_traveller_memo(m, n - 1, memo)
        memo[(m, n)] = value

    return value
