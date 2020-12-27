"""
Python implementation of the first and the nineth chapters code.
Original videos can be viewed from the following link:
https://www.youtube.com/watch?v=oBt53YbR9Kk
"""

# First Chapter
def fib(n: int):

    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)

def mem_fib(n: int, memo: dict={}):

    result = memo.get(n)
    if not result:
        if n <= 2:
            result = 1
        else:
            result = mem_fib(n - 1, memo) + mem_fib(n - 2, memo)
        memo[n] = result

    return memo[n]


# Nineth Chapter
def tab_fib(n: int):

    table = [0 for _ in range(n + 1)]
    table[1] = 1
    for i in range(n):
        table[i + 1] += table[i]
        if i + 1 == n:
            break
        table[i + 2] += table[i]

    return table[n]