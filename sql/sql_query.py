# -*- coding: utf-8 -*-
__author__ = 'legenove'


class Mtest():
    def __init__(self, a):
        self.data = a

    # def __cmp__(self, other):
    #     print self.data
    #     return 'self.data == other'

    def __eq__(self, other):
        return 'self.data == other'

c = [1]
a = Mtest(c)
b = Mtest(c)

print Mtest(c) == '1'
