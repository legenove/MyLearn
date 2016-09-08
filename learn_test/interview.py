__author__ = 'legenove'


def extendList(val, list=[]):
    list.append(val)
    return list


list1 = extendList(10)
list2 = extendList(123, [])
list3 = extendList('a')

print list1
print list2
print list3


def multipliers():
    return [lambda x: x * i for i in range(4)]


print multipliers()
print [m(2) for m in multipliers()]


class Parent(object):
    x = 1


class Child1(Parent):
    pass


class Child2(Parent):
    pass


print Parent.x, Child1.x, Child2.x
Child1.x = 2
print Parent.x, Child1.x, Child2.x
Parent.x = 3
print Parent.x, Child1.x, Child2.x


class Temp(object):
    _x = 0
    _my_sum = 0

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            orig = super(Temp, cls)
            cls._instance = orig.__new__(cls, *args, **kwargs)
        else:
            cls._x += 1
            cls._my_sum += cls._x
        return cls._instance

    @classmethod
    def my_sum(cls):
        return cls._my_sum

    @classmethod
    def x(cls):
        return cls._x


print "mysum = ", Temp.my_sum(), Temp.x()

list4 = ['a', 'b', 'c', 'd', 'e']
print list4[10:]

n = [1, 2, 5, 10, 3, 100, 9, 24]

# for e in n:
# if e < 5:
# n.remove(e)
# print n
m = []
for e in n:
    if e > 5:
        m.append(e)
print m

import copy

al = [[1], [2], [3]]
bl = copy.copy(al)
cl = copy.deepcopy(al)

print "before=>"
print al
print bl
print cl

al[0][0] = 0
al[1] = None

print "after=>"
print al
print bl
print cl


def ChangeList(a):
    a = [4]


def ChangeListin(a):
    a[0] = 10

import httplib

lstFoo = [2]
ChangeList(lstFoo)
print lstFoo
ChangeListin(lstFoo)
print lstFoo

m = 2
n = 5
print reduce(lambda x, y: x * y, range(1, n + 1), m)

dict = {"a": "apple", "b": "banana", "c": "grape", "d": "orange"}
print dict.iteritems()
for k, v in dict.iteritems():
    print "dict[%s] =" % k, v
for (k, v) in zip(dict.iterkeys(), dict.itervalues()):
    print "dict[%s] =" % k, v

print dict.items()
i = 10
count = 0
while i:
    if i & 1:
        count += 1
    i = i >> 1
print count

a = [0, 1, 2, 3]
print a[4:]
print a[3:]
a.reverse()

