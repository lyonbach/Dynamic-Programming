"""
Python implementation of the code for the sixth chapter.
Original videos can be viewed from the following link:
https://www.youtube.com/watch?v=oBt53YbR9Kk
"""

def can_construct(target: str, word_bank: list):

    """
    Returns if target string can be constructed from the given words.
    Returns bool.
    """

    if target == '':
        return True

    for prefix in word_bank:
        if target.startswith(prefix):
            suffix = target[target.index(prefix) + len(prefix):]
            result = can_construct(suffix, word_bank)
            if result:
                return True

    return False


def mem_can_construct(target: str, word_bank: list, memo={}):

    """
    Returns if target string can be constructed from the given words.
    Returns bool.
    """

    if target in memo:
        return memo[target]

    if target == '':
        return True

    for prefix in word_bank:
        if target.startswith(prefix):
            suffix = target[target.index(prefix) + len(prefix):]
            result = mem_can_construct(suffix, word_bank, memo)
            memo[target] = result
            if result:
                return True

    return False
