"""
Python implementation of the seventh and the fifteenth chapters' code.
Original videos can be viewed from the following link:
https://www.youtube.com/watch?v=oBt53YbR9Kk
"""

# Seventh Chapter
def count_construct(target: str, word_bank: list):

    """
    Returns number of ways that target string can be constructed using strings from the word_bank.
    Returns int.
    """

    if target == '':
        return 1

    total_count = 0

    for prefix in word_bank:
        if target.startswith(prefix):
            new_target = target[target.index(prefix) + len(prefix):]
            total_count += count_construct(new_target, word_bank)

    return total_count


def mem_count_construct(target: str, word_bank: list, memo={}):

    """
    Returns number of ways that target string can be constructed using strings from the word_bank.
    Returns int.
    """

    if target in memo:
        return memo[target]

    if target == '':
        return 1

    total_count = 0

    for prefix in word_bank:
        if target.startswith(prefix):
            new_target = target[target.index(prefix) + len(prefix):]
            total_count += mem_count_construct(new_target, word_bank, memo)

    memo[target] = total_count
    return total_count


def tab_count_construct(target: str, word_bank: list):

    """
    Returns number of ways that target string can be constructed using strings from the word_bank.
    Returns int.
    """

    table = [0 for _ in range(len(target) + 1)]
    table[0] = 1
    
    for idx in range(len(table)):
        suffix = target[idx:]
        for prefix in word_bank:
            target_idx = idx + len(prefix)
            if target_idx >= len(table):
                continue
            if not suffix.startswith(prefix):
                continue
            table[target_idx] = table[target_idx] + table[idx]

    return table[-1]
