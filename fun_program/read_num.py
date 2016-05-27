# -*- coding: utf-8 -*-
__author__ = 'legenove'

import sys

NUM = 6
LINE_NUM = 70

MaxNum = 1 << NUM
numList = range(0, MaxNum)

resultNum = 0
ready = "n"

print "Please think of a number in range 0 to 63"
while ready != "y":
    ready = raw_input("Are you ready(y/n)?")

for x in range(0, NUM):
    print "=" * LINE_NUM
    tmpSet = set([(tmpNum | 1 << x) for tmpNum in numList])
    for i, k in enumerate(list(tmpSet)):
        sys.stdout.write("%d\t\t" % k)
        if (i + 1) % 8 == 0:
            print ""
    print "=" * LINE_NUM
    print ""

    tmpStr = raw_input("Is the number in list? n(y/n)?\n")
    tmpStr = tmpStr.strip()
    if tmpStr == "y":
        resultNum += 1 << x

print "The number is: %d" % resultNum