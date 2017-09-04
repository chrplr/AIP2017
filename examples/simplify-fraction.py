""" Simplification of fractions """

# Read the fraction

a = int(input("numerator? "))
b = int(input("denominator? "))

# A first solution is to divide the numerator and denominator by their gcd 

from math import gcd

c = gcd(a, b)
print("{}/{}".format(a // c, b // c))

# A second solution relies on the existence of the *fractions* module

from fractions import Fraction

d = Fraction(a, b)
print(d)
