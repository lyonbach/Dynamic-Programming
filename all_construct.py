"""
Python implementation of the code for the eighth chapter.
Original videos can be viewed from the following link:
https://www.youtube.com/watch?v=oBt53YbR9Kk
"""

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
