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
