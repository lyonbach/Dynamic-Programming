"""
Python implementation of the sixth and the fourteenth chapters code.
Original videos can be viewed from the following link:
https://www.youtube.com/watch?v=oBt53YbR9Kk
"""

# Sixth Chapter
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


# Fourteenth Chapter
def tab_can_construct(target: str, word_bank: list):

    """
    Returns if target string can be constructed from the given words.
    Returns bool.
    """

    table = [False for _ in range(len(target) + 1)]
    table[0] = True

    for idx in range(len(target)):
        if table[idx] is True:
            suffix = target[idx:]
            for prefix in word_bank:
                if idx + len(prefix) >= len(table):
                    continue
                if not suffix.startswith(prefix):
                    continue
                table[idx + len(prefix)] = True

    return table[-1]
