# -*- coding:utf-8 -*-
__author__ = 'legenove'

# gcd function
def gcd(m, n):
    while m % n != 0:
        old_m = m
        old_n = n
        m = old_n
        n = old_m % old_n
    return n

# test
print gcd(8, 6)

# Fraction class
# Implements: addition and equality
# To do: multiplication, division, subtraction and comparison operators (< , >)
class Fraction(object):
    def __init__(self, top, bottom):
        common = gcd(top, bottom)
        self._num = top / common
        self._den = bottom / common

    def __str__(self):
        return str(self._num) + '/' + str(self._den)

    def __add__(self, other):
        new_num = self._num * other.den + self._den * other.num
        new_den = self._den * other.den
        return Fraction(new_num, new_den)

    def __sub__(self, other):
        new_num = self._num * other.den - self._den * other.num
        new_den = self._den * other.den
        return Fraction(new_num, new_den)

    def __mul__(self, other):
        return Fraction(self._num * other.num, self._den * other.den)

    def __div__(self, other):
        return Fraction(self._num * other.den, self._den * other.num)


    def __eq__(self, other):
        return (self._num * other.den) == (self._den * other.num)

    @property
    def num(self):
        return self._num

    @num.setter
    def num(self, value):
        self._num = value

    @num.deleter
    def num(self):
        del self._num

    @property
    def den(self):
        return self._den

    @den.setter
    def den(self, value):
        self._den = value

    @den.deleter
    def den(self):
        del self._den


x = Fraction(1, 2)
y = Fraction(2, 3)
z = Fraction(4, 6)

print(x + y)
print(x == y)
print(z == y)
print(y - x)
print(y * x)
print(y / x)