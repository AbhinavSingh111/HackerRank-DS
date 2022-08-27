# https://www.hackerrank.com/challenges/reduce-function/problem?isFullScreen=true&utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
# Given a list of rational numbers,find their product.

# The reduce() function applies a function of two arguments cumulatively on a list of objects in succession from left to right to reduce it to one value. 
# Say you have a list, say [1,2,3] and you have to find its sum.

from fractions import Fraction
from functools import reduce

def product(fracs):
    t = reduce(lambda x,y:x*y , fracs)
    return t.numerator, t.denominator

if __name__ == '__main__':
