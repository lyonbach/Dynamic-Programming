"""
Python implementation of the first chapter code.
Original videos can be viewed from the following link:
https://www.youtube.com/watch?v=oBt53YbR9Kk
"""

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
