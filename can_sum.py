"""
Python implementation of the third and the eleventh chapters code.
Original videos can be viewed from the following link:
https://www.youtube.com/watch?v=oBt53YbR9Kk
"""

# Third Chapter
def can_sum(target_sum: int, numbers: list):

    """
    Returns a boolean value indicating if it is possible to get the given target_sum from the given list of numbers.
    """

    if target_sum == 0:
        return True

    if target_sum < 0:
        return False

    for num in numbers:
        remainder = target_sum - num  # remainedar will be the target for the recursive function.
        if (can_sum(remainder, numbers)):
            return True

    return False

def mem_can_sum(target_sum: int, numbers: list, memo: dict=None):

    """
    Returns a boolean value indicating if it is possible to get the given target_sum from the given list of numbers.
    """

    memo = {} if memo is None else memo

    if target_sum in memo:
        return memo[target_sum]

    if target_sum == 0:
        return True

    if target_sum < 0:
        return False

    for num in numbers:
        remainder = target_sum - num  # remaindar will be the target for the recursive function.
        if mem_can_sum(remainder, numbers, memo):
            memo[target_sum] = True
            return True

    memo[target_sum] = False
    return False


# Eleventh Chapter
def tab_can_sum(target_sum: int, numbers: list):

    """
    Returns a boolean value indicating if it is possible to get the given target_sum from the given list of numbers.
    Non-Recursive implementation.
    """

    if target_sum < 0:
        return False

    table = [bool(idx in numbers) for idx in range(target_sum + 1)]
    table[0] = True
    
    for idx in range(target_sum + 1):
        for number in numbers:
            if idx + number > target_sum:
                continue
            table[idx + number] |= table[idx]
    return table[target_sum]
