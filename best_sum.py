"""
Python implementation of the fifth and the thirteenth chapters code.
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

def mem_best_sum(target_sum: int, numbers: list, memo: dict=None):

    """
    Returns a list containing "shortest" combination of elements that add up to exactly as input target_sum.
    Returns None if target_sum can not be reached.
    """

    memo = {} if memo is None else memo
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

def tab_best_sum(target_sum: int, numbers: list):

    """
    Returns a list containing "shortest" combination of elements that add up to exactly as input target_sum.
    Returns None if target_sum can not be reached.
    """

    table = [None for _ in range(target_sum + 1)]
    table[0] = []

    for idx in range(target_sum + 1):
        for number in numbers:
            if idx + number > target_sum:
                break
            if table[idx] is None:
                continue

            current_list = list(table[idx]) + [number] # We need to copy the list, not change it.
            if table[idx + number] is None or len(table[idx + number]) > len(current_list):
                 table[idx + number] = current_list
    return table[-1]
