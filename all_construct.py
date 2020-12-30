"""
Python implementation of the eighth and the sixteenth chapters' code.
Original videos can be viewed from the following link:
https://www.youtube.com/watch?v=oBt53YbR9Kk
"""

# Eighth Chapter
def all_construct(target: str, word_bank: list):

    """
    Returns a list of lists of that consist a combination of which that the target string can be constructed using strings from the word_bank.
    """

    if target == '':
        return [[]]

    result = []
    for prefix in word_bank:
        if target.startswith(prefix):
            suffix = target[target.index(prefix) + len(prefix):]
            suffix_combinations = all_construct(suffix, word_bank)
            target_combinations = [[prefix] + s_comb for s_comb in suffix_combinations]
            result.extend(target_combinations)

    return result



def mem_all_construct(target: str, word_bank: list, memo={}):

    """
    Returns a list of lists of that consist a combination of which that the target string can be constructed using strings from the word_bank.
    """

    if target in memo:
        return memo[target]

    if target == '':
        return [[]]

    result = []
    for prefix in word_bank:
        if target.startswith(prefix):
            suffix = target[target.index(prefix) + len(prefix):]
            suffix_combinations = mem_all_construct(suffix, word_bank, memo)
            target_combinations = [[prefix] + s_comb for s_comb in suffix_combinations]
            result.extend(target_combinations)
            memo[target] = result

    return result


# Sixteenth Chapter
def tab_all_construct(target: str, word_bank: list):

    """
    Returns a list of lists of that consist a combination of which that the target string can be constructed using strings from the word_bank.
    """
    
    table = [[] for _ in range(len(target) + 1)]
    table[0].append([])

    for idx in range(len(table)):
        suffix = target[idx:]
        for prefix in word_bank:
            target_idx = idx + len(prefix)
            if target_idx >= len(table):
                continue
            if not suffix.startswith(prefix):
                continue
            # Following line takes the current position elements (list(str)))and target position elements (list(str))
            # from the table, and appends current prefix to each. Then finally replaces the target items with the
            # resulting items.
            table[target_idx].extend([list(item) + [prefix] for item in list(table[idx])])

    return table[-1]
