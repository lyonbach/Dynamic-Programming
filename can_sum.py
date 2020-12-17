"""
Python implementation of the code for the third chapter.
Original videos can be viewed from the following link:
https://www.youtube.com/watch?v=oBt53YbR9Kk
"""

def can_sum(target_sum: int, numbers: list):

    if target_sum == 0:
        return True

    if target_sum < 0:
        return False

    for num in numbers:
        remainder = target_sum - num  # remainedar will be the target for the recursive function.
        if (can_sum(remainder, numbers)):
            return True

    return False

def mem_can_sum(target_sum: int, numbers: list, memo: dict={}):

    if target_sum in memo.keys():
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
