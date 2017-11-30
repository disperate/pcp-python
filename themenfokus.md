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

### Decorators

### Function caching
