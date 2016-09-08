# -*-coding:utf-8-*-
__author__ = 'legenove'


# sort and sorted
# sort 原地排序，需要可变的序列
# sorted 返回一个list

a = (1, 3, 2, 4)

# a.sort() has no attribute

print sorted(a)
print a

from collections import Counter

c = Counter('success')
print c
c.update('successfully')
print c
c.subtract('successfully')
print c

