# Prolog Uebung 3+4 Aufgabe 2 in Python
import time
import sys
from functools import lru_cache


# maxsize defines how many recent return values to cache.
@lru_cache(maxsize=2)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


# Set a higher Recursion Limit (normal: 1000)
sys.setrecursionlimit(10000)

t1 = time.time()*1000
print(fib(1000))
t2 = time.time()*1000
print('{}{}'.format("Time for 1st calculation: ", t2-t1))
print(fib(1000))
t3 = time.time()*1000
print('{}{}'.format("Time for 2nd calculation: ", t3-t2))

# clear cache:
fib.cache_clear()

print(fib(1000))
t4 = time.time()*1000
print('{}{}'.format("Time for 3rd calculation: ", t4-t3))
