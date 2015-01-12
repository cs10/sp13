# CS10 Beyond Blocks: Python : Session #1 by Michael Ball is licensed under a
# Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License.

def fib(n):
    if (n <= 1):
        return n
    else:
        return fib(n - 1) + fib(n - 2)

def i_fib(n):
    a,b = 0,1
    for _ in range(n):
        a,b = b, a + b
    return a

def pr_fib(s=None):
    if (s == "r"):
        for i in range(1000):
            print(fib(i))
    else:
        for i in range(1000):
            print(i_fib(i))
