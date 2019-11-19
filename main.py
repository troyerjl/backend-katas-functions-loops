#!/usr/bin/env python

__author__ = "troyerjl"


def add(x, y):
    product = x + y
    return product


def helper_multiply(x, y):
    product = 0
    for i in range(0, abs(y)):
        product += x
    return product


def multiply(x, y):
    product = helper_multiply(x, y)
    if x >= 0 and y >= 0:
        return product
    elif x < 0 and y < 0:
        return abs(product)
    elif x < 0 or y > 0:
        return product
    elif x > 0 and y < 0:
        return -product


def power(x, n):
    product = 1
    for i in range(0, n):
        product = multiply(product, x)
    return product


def factorial(x):
    product = 1
    for i in range(1, x+1):
        product = multiply(product, i)
    return product


def fibonacci(n):
    a, b = 1, 1
    if n == 0:
        return b
    elif n == 1:
        return b
    else:
        for i in range(2, n):
            c = add(a, b)
            a = b 
            b = c 
        return b 


if __name__ == '__main__':
    # your code to call functions above
    pass
