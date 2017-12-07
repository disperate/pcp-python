# Themenliste

### Einführung

- Python 2.X & Python 3.X
- Monty Python's Flying Circus

### Einrückung (Indentation)
Spaces are the preferred indentation method.  
Tabs should be used solely to remain consistent with code that is already indented with tabs.  
Python 3 disallows mixing the use of tabs and spaces for indentation.

![Linksvstabs](http://meh.schizofreni.co/img/tabs-spaces-both.png)
### Typisierung & Duck Typing
Python is dynamically but strongly typed.
```python
variable = 3
type(variable)
variable = 'hello'
type(variable)
```

```python
number = 3
numberString = '3'

## print(number + numberString)
## TypeError: unsupported operand type(s) for +: 'int' and 'str'

print(number + int(numberString))
print(str(number) + numberString)
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

```python
# in python functions are higher-order function
# they can be a parameter

import time

def time_messuring(some_function):

    def wrapper():
        t1 = time.time()
        some_function()
        t2 = time.time()
        print(some_function.__name__ + " took " + str((t2 - t1)) + " seconds" + "\n")

    return wrapper

@time_messuring
def sleep_time():
    time.sleep(0.1)
    print("Wheee!")

# sleep_time = time_messuring(sleep_time)

sleep_time()
```
Real world example from [Flask]([http://flask.pocoo.org/]), a popular python web framework.

```python
@app.route('/grade', methods=['POST'])
@login_required
@validate_json('student_id')
def update_grade():
    json_data = request.get_json()
    print(json_data)
    [...]
```

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
