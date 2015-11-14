# -*- coding: utf-8 -*-
__author__ = 'legenove'

#class
class Fraction(object):
    def __init__(self, top, bottom):
        common = gcd(top, bottom)
        self._num = top / common
        self._den = bottom / common

    ###1.class __str__####
    def __str__(self):
        return str(self._num) + "/" + str(self._den)

    ###2.class __add__#### __sub__,__mul__,__div__
    def __add__(self, other):
        new_num = self._den * other.num + self._num * other.den
        new_den = self._den * other.den

        return Fraction(new_num, new_den)

    def __sub__(self, other):
        return Fraction(self._den * other.num - self._num * other.den, self._den * other.den)

    def __mul__(self, other):
        return Fraction(self._num * other.num, self._den * other.den)

    def __div__(self, other):
        return Fraction(self._num * other.den, self._den * other.num)

    ###4.equal __eq__####
    # 相等	x == y	x.__eq__(y)
    # 不相等	x != y	x.__ne__(y)
    # 小于	x < y	x.__lt__(y)
    # 小于或等于	x <= y	x.__le__(y)
    # 大于	x > y	x.__gt__(y)
    # 大于或等于	x >= y	x.__ge__(y)
    # 布尔上上下文环境中的真值	if x:	x.__bool__()
    #####################
    def __eq__(self, other):
        first_num = self._num * other.den
        secend_num = self._den * other.num
        return first_num == secend_num

    def __lt__(self, other):
        return self._num * other.den < self._den * other.num

    def __le__(self, other):
        return self._num * other.den <= self._den * other.num

    # def __ge__(self, other):
    #     return self._num * other.den >= self._den * other.num
    #
    # def __gt__(self, other):
    #     return self._num * other.den > self._den * other.num

    ###5.property ###
    def getnum(self):
        return self._num

    def setnum(self, value):
        self._num = value

    def delnum(self):
        del self._num

    num = property(getnum, setnum, delnum, 'set _num')

    @property
    def den(self):
        return self._den

    @den.setter
    def den(self, value):
        self._den = value

    @den.deleter
    def den(self):
        del self._den


###3.GCD 最大公约数####
def gcd(m, n):
    while m % n != 0:
        old_m = m
        old_n = n

        m = old_n
        n = old_m % n
    return n

#1.test
a = Fraction(3, 5)
b = Fraction(4, 5)
d = Fraction(6, 10)
print a
print d
#2.test
c = d + b
# d = a * b
# print d
print c
#3.test
print(gcd(6, 8))
#4.test
print (a == b)
print (a == d)
print (a < d)
print (a <= d)
print (a > d)
print (a >= d)

#5.test
print a.den
a.num = 7
print a
print(a == c)