"""
Python implementation of the code for the fifth chapter.
Original videos can be viewed from the following link:
https://www.youtube.com/watch?v=oBt53YbR9Kk
"""

import copy

def best_sum(target_sum: int, numbers: list):

    """
    Returns a list containing "shortest" combination of elements that add up to exactly as input target_sum.
    Returns None if target_sum can not be reached.
    """

    if target_sum == 0:
        return []

    if target_sum < 0:
        return None

    shortest_result = None
    for num in numbers:
        remainder = target_sum - num
        remainder_result = best_sum(remainder, numbers)
        if remainder_result is not None:
            remainder_result.append(num)
            if shortest_result is None:
                shortest_result = remainder_result
            elif len(shortest_result) >= len(remainder_result):
                shortest_result = remainder_result

    return shortest_result

def mem_best_sum(target_sum: int, numbers: list, memo: dict={}):

    """
    Returns a list containing "shortest" combination of elements that add up to exactly as input target_sum.
    Returns None if target_sum can not be reached.
    """

    if target_sum in memo:
        return memo[target_sum]

    if target_sum == 0:
        return []

    if target_sum < 0:
        return None

    shortest_result = None
    for num in numbers:
        remainder = target_sum - num
        remainder_result = copy.copy(mem_best_sum(remainder, numbers, memo))
        if remainder_result is not None:
            remainder_result.append(num)
            if shortest_result is None:
                shortest_result = copy.copy(remainder_result)
            elif len(shortest_result) >= len(remainder_result):
                shortest_result = copy.copy(remainder_result)

    memo[target_sum] = shortest_result
    return shortest_result

# Notice slightly modified code at lines 54, 58 and 60.
# This is because Python is passing lists by reference and we could not be exactly same as in the series.
