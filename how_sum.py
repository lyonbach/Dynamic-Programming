"""
Python implementation of the fourth and the twelfth chapters code.
Original videos can be viewed from the following link:
https://www.youtube.com/watch?v=oBt53YbR9Kk
"""

# Fourth Chapter
def how_sum(target_sum: int, numbers: list):

    """
    Returns a list containing any combination of elements that add up to exactly as input target_sum.
    Returns None if target_sum can not be reached.
    """
    
    if target_sum == 0:
        return []

    if target_sum < 0:
        return None

    for num in numbers:
        remainder = target_sum - num
        remainder_result = how_sum(remainder, numbers)
        if remainder_result is not None:
            remainder_result.append(num)
            return remainder_result

    return None

def mem_how_sum(target_sum: int, numbers: list, memo: dict=None):

    """
    Returns a list containing any combination of elements that add up to exactly as input target_sum.
    Returns None if target_sum can not be reached.
    """

    memo = {} if memo is None else memo

    if target_sum in memo:
        return memo[target_sum]

    if target_sum == 0:
        return []

    if target_sum < 0:
        return None

    for num in numbers:
        remainder = target_sum - num
        remainder_result = mem_how_sum(remainder, numbers, memo)
        if remainder_result is not None:
            remainder_result.append(num)
            memo.update({target_sum: remainder_result})
            return remainder_result
    memo.update({target_sum: None})
    return None


# Twelfth Chapter
def tab_how_sum(target_sum: int, numbers: list):

    """
    Returns a list containing any combination of elements that add up to exactly as input target_sum.
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
            if table[idx + number] is None:
                table[idx + number] = list(table[idx]) + [number] # We need to copy the list, not change it.

    return table[target_sum]
