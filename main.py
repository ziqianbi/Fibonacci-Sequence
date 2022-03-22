from functools import lru_cache

@lru_cache
def fib_recursion(n):
    # Boundary conditions
    if n < 1 or int(n) != n: return 'error, the sequence starts at int(1)'
    return 1 if n in (1, 2) else fib_recursion(n - 1) + fib_recursion(n - 2)

def fib_func(n):
    if n < 1 or int(n) != n: return 'error, the sequence starts at int(1)'
    
    a, b = 1, 1
    for i in range(n-2):
        a, b = a + b, a
    return a

if __name__ == '__main__':

    for i in range(10):
        print(i, fib_recursion(i))

    print()

    for i in range(10):
        print(i, fib_func(i))
