"""
Python implementation of the code for the fourth chapter.
Original videos can be viewed from the following link:
https://www.youtube.com/watch?v=oBt53YbR9Kk
"""

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

def mem_how_sum(target_sum: int, numbers: list, memo: dict):

    """
    Returns a list containing any combination of elements that add up to exactly as input target_sum.
    Returns None if target_sum can not be reached.
    """

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
