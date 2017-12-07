from random import randint


# a generator that yields items instead of returning a list
def yieldRandomInt():
  while True:
    x = randint(0, 100000)
    yield x
    print(x)


res = yieldRandomInt()
for i in res:
    if 1200 <= i <= 1400:
        print(i)
        break