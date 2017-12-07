# Java Uebung 1+2 Aufgabe 2
# List comprehension


def printNumberAndSquare(myList):
    s = [[x, x**2] for x in myList]
    print(s)


def printNumberAndSquareV2(myList):
    [print(x[0], ":", x[1]) for x in [[x, x**2] for x in myList]]


l = [1, 2, 3, 5, 8]
printNumberAndSquare(l)
printNumberAndSquareV2(l)

V = [2**i for i in range(13)]
print(V)
M = [x for x in range(50) if x % 2 == 0]
print(M)
