# Themenliste

### Einführung

- Python 2.X & Python 3.X
- Monty Python's Flying Circus

### Einrückung (Indentation)

### Typisierung & Duck Typing
```python
# Python is dynamically but strongly typed.
variable = 3
variable = 'hello'
```
### yield-Anweisung & Generatoren (Coroutinen)
```python
# a generator that yields items instead of returning a list
def firstn(n):
  num = 0
  while num < n:
    yield num
    num += 1

sum_of_first_n = sum(firstn(1000000))
```
Inspired by [https://wiki.python.org/moin/Generators](https://wiki.python.org/moin/Generators)
### List comprehension
```python
S = [x**2 for x in range(10)]
> [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

V = [2**i for i in range(13)]
> [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]

M = [x for x in S if x % 2 == 0]
> [0, 4, 16, 36, 64]
```
### Decorators

### Function caching

```python
from functools import lru_cache

#maxsize defins how many recent return values to cache.
@lru_cache(maxsize=32)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print([fib(n) for n in range(10)])
# clear cache:
fib.cache_clear()
```
Inspired by [http://book.pythontips.com/en/latest/function_caching.html](http://book.pythontips.com/en/latest/function_caching.html)
