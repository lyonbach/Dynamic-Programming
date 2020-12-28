"""
Python implementation of the second chapter code.
Original videos can be viewed from the following link:
https://www.youtube.com/watch?v=oBt53YbR9Kk
"""

def grid_traveller(m: int, n: int):

    """
    Returns the number of ways as int within the given grid size.
    Assumes that initial location is 0, 0 (top left).
    """

    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    return grid_traveller(m - 1, n) + grid_traveller(m, n - 1)


def mem_grid_traveller(m: int, n: int, memo: dict={}):

    """
    Returns the number of ways as int within the given grid size.
    Assumes that initial location is 0, 0 (top left).
    """

    value = memo.get((m, n))
    if not value:
        if m == 1 and n == 1:
            value = 1
        elif m == 0 or n == 0:
            value = 0
        else:
            value = mem_grid_traveller(m - 1, n, memo) + mem_grid_traveller(m, n - 1, memo)
        memo[(m, n)] = value

    return value
