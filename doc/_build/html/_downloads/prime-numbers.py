""" 
list the prime numbers between 1 and 1000.

list the prime numbers between 1 and 1000.
"""

import math


def is_factor(a, b):
    return b % a == 0


def methode_pedestre():
    premiers = [1]
    
    for n in range(2, 1001):
        prime = True
        for i in range(2, n):
            if is_factor(i , n):
                prime = False
                break
        if prime:
            premiers.append(n)

    return premiers

import numpy

def crible_erathostene(max):
    premiers = [True] * (max) 
    for i in range(2, int(math.sqrt(max)) + 1):
        if premiers[i]:
            for j in [(i**2 + p * i) for p in range(1, max//i)]:
                if j >= max:
                    break
                premiers[j] = False       
    return numpy.arange(max)[premiers]


print(crible_erathostene(100))
