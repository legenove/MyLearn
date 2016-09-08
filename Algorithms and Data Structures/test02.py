# -*- coding:utf-8 -*-
__author__ = 'legenove'
from timeit import Timer


def anagram_solution1(s1, s2):
    a_list = list(s2)
    pos_1 = 0
    still_ok = True
    while pos_1 < len(s1) and still_ok:
        pos_2 = 0
        found = None
        while pos_2 < len(a_list) and not found:
            if s1[pos_1] == a_list[pos_2]:
                found = True
            else:
                pos_2 += 1

        if found:
            a_list[pos_2] = None
            pos_1 += 1
        else:
            still_ok = False
    return still_ok


print anagram_solution1('1234', '2341')


def anagram_solution2(s1, s2):
    a_list_1 = list(s1)
    a_list_2 = list(s2)

    a_list_1.sort()
    a_list_2.sort()

    pos = 0
    matches = True

    while pos < len(a_list_1) and matches:
        if a_list_1[pos] == a_list_2[pos]:
            pos += 1
        else:
            matches = False
    return matches


print(anagram_solution2('abcde', 'edcba'))


def anagram_solution3(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26

    for s in s1:
        c1[ord(s) - ord('a')] += 1
    for s in s2:
        c2[ord(s) - ord('a')] += 1
    j = 0
    still_ok = True
    while j < len(c1) and still_ok:
        if c1[j] == c2[j]:
            j += 1
        else:
            still_ok = False
    return still_ok


print(anagram_solution3('apple', 'pleap'))


print list(range(2))

def test1():
    l = []
    for i in range(10000):
        l += [i]


def test2():
    l = []
    for i in range(10000):
        l.append(i)


def test3():
    l = [i for i in range(10000)]


def test4():
    l = list(range(10000))


t1 = Timer("test1()", "from __main__ import test1")
print("concat ", t1.timeit(number=1000), "milliseconds")
t2 = Timer("test2()", "from __main__ import test2")
print("append ", t2.timeit(number=1000), "milliseconds")
t3 = Timer("test3()", "from __main__ import test3")
print("comprehension ", t3.timeit(number=1000), "milliseconds")
t4 = Timer("test4()", "from __main__ import test4")
print("list range ", t4.timeit(number=1000), "milliseconds")

import timeit
import random

for i in range(10000, 1000001, 20000):
    t = timeit.Timer("random.randrange(%d) in x" % i,
                     "from __main__ import random,x")
    x = list(range(i))
    lst_time = t.timeit(number=1000)
    x = {j: None for j in range(i)}
    d_time = t.timeit(number=1000)
    print("%d,%10.3f,%10.3f" % (i, lst_time, d_time))

