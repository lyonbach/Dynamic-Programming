#!./interpreter/bin/python

import fibo as fb
import grid_traveller as gt
import can_sum as cs
import how_sum as hs
import best_sum as bs
import can_construct as cc
import count_construct as cnc
import all_construct as ac

TEST_SEPERATOR = '_' * 120 + '\n'
FUNCTION_SEPERATOR = '=' * 120 + '\n'


def test_one(function, info):

    for inputs_, expected in list(info):
        print(f"Input: {inputs_}")
        if isinstance(inputs_, int):
            result = function(inputs_)
        else:
            result = function(*inputs_)
        print(f"Expected: {expected}")
        print(f"Returned: {result}")
        print(TEST_SEPERATOR)
#        assert result == expected



def run_tests(**kwargs):

    module = kwargs.get("module")
    functions = kwargs.get("functions")
    inputs = kwargs.get("inputs")
    outputs = kwargs.get("outputs")

    for function in functions:
        print(f"Module  : {module.__name__}")
        print(f"Function: {function.__name__}\n")
        print(f"Doc: {function.__doc__}")
        test_one(function, zip(inputs, outputs))
        print(FUNCTION_SEPERATOR)


if __name__ == "__main__":

    all_test_infos = []

    # fibo
    test_info = {
        "module": fb,
        "functions": (fb.fib, fb.mem_fib, fb.tab_fib),
        "inputs": (
            6,
            7,
            8,
        #    50,
        ),
        "outputs": (8, 13, 21, 12586269025),
    }
    all_test_infos.append(test_info)


    # grid traveller
    kwargs = {
        "module": gt,
        "functions": (gt.tab_grid_traveller, gt.mem_grid_traveller, gt.grid_traveller),
        "inputs": (
            (1, 1),
            (2, 3),
            (3, 2),
            (3, 3),
    #        (18, 18),
        ),
        "outputs": (1, 3, 3, 6, 2333606220)
    }
    all_test_infos.append(test_info)


    # can sum
    test_info = {
        "module": cs,
        "functions": (cs.can_sum, cs.mem_can_sum, cs.tab_can_sum),
        "inputs": (
            (7, (2, 3)),
            (7, [5, 3, 4, 7]),
            (7, [2, 4]),
            (8, [2, 3, 5]),
    #        (300, [7, 14]),
        ),
        "outputs": (True, True, False, True, False),
    }
    all_test_infos.append(test_info)


    # how sum
    test_info = {
        "module": hs,
        "functions": (hs.tab_how_sum, hs.mem_how_sum, hs.how_sum),
        "inputs": (
            (0, [5, 100]),
            (5, [2]),
            (7, [2, 3]),
            (7, [5, 3, 4, 7]),
            (7, [2, 4]),
            (8, [2, 3, 5]),
            (294, [7, 14]),
    #        (300, [7, 14]),
            ),
        "outputs": (
            [],
            None,
            [3, 2, 2],
            [7],
            None,
            [3, 5],
            [14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14],
            None,
        ),
    }
    all_test_infos.append(test_info)


    # best sum
    test_info = {
        "module": bs,
        "functions": (bs.tab_best_sum, bs.mem_best_sum, bs.best_sum),
        "inputs": (
            (0,   [5, 3, 4, 7]),
            (7,   [5, 3, 4, 7]),
            (8,   [2, 3, 5, 1 ,1]),
            (8,   [1, 4, 5, 5]),
    #        (100, [1, 2, 5, 25]),
            ),
        "outputs": (
            [],
            [7],
            [3, 5],
            [4, 4],
            [25, 25, 25, 25],
        ),
    }
    all_test_infos.append(test_info)


    # can construct
    test_info = {
        "module": cc,
        "functions": (cc.tab_can_construct, cc.mem_can_construct, cc.can_construct),
        "inputs": (
            ("abcdef", ['ab', "abc", "cd", "def", "abcd"]),
            ("skateboard", ["bo", "rd", "ate", "t", "ska",  "sk", "boar"]),
            ("enterapotentpot", ['a', 'p', "ent", "enter", "ot", 'o',  't']),
    #        ("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ['e', "ee", "eee", "eeee", "eeeee", "eeeeee"]),
            ),
        "outputs": (True, False, True, False),
    }
    all_test_infos.append(test_info)


    # count construct
    test_info = {
        "module": cnc,
        "functions": (cnc.tab_count_construct, cnc.mem_count_construct, cnc.count_construct),
        "inputs": (
            ("purple", ["purp", 'p', "ur", "le", "purpl"]),
            ("abcdef", ['ab', "abc", "cd", "def", "abcd"]),
            ("skateboard", ["bo", "rd", "ate", "t", "ska",  "sk", "boar"]),
            ("enterapotentpot", ['a', 'p', "ent", "enter", "ot", 'o',  't']),
    #        ("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ['e', "ee", "eee", "eeee", "eeeee", "eeeeee"])
            ),
        "outputs": (2, 1, 0, 4, 0),
    }
    all_test_infos.append(test_info)


    # all construct
    test_info = {
        "module": ac,
        "functions": (ac.tab_all_construct, ac.mem_all_construct, ac.all_construct),
        "inputs": (
            ("abcdef", ['ab', "abc", "cd", "def", "abcd", "ef", 'c']),
            ("skateboard", ["bo", "rd", "ate", "t", "ska",  "sk", "boar"]),
            ("purple", ["purp", 'p', "ur", "le", "purpl"]),
    #        ("aaaaaaaaaaaaaaaaaaaaaaaaaaz", ['a', 'aa', "aaa", "aaaa", "aaaaa"])
            ),
        "outputs": (
            [
                ['ab', 'cd', 'ef'],
                ['ab', 'c', 'def'],
                ['abc', 'def'],
                ['abcd', 'ef']
            ],
            [],  # results for skateboard
            [
                ["purp", "le"],
                ['p', "ur", 'p', "le"],
            ],
            []  # results for aaaaaaaaaaaaaaaaaaaaaaaaaaz
        ),
    }
    all_test_infos.append(test_info)


    # Comment/Uncomment the individual test info that you want to disable/enable.
    # Additionally some inputs are disabled due to very high time/space complexity in various functions,
    # Remove the commented inputs to enable them.

    for test_info in all_test_infos:
        run_tests(**test_info)
