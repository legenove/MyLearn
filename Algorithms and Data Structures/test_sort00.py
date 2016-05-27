# -*- coding:utf-8 -*-
__author__ = 'legenove'

# 直接插入排序
# print "o(n)"
# print "o(n^2)"
def insert_sort(l):
    for i in range(len(l)):
        key = l[i]
        j = i - 1
        while j >= 0 and key < l[j]:
            l[j], l[j + 1] = l[j + 1], l[j]
            j -= 1

    return l


# shell排序
def shell_pass(mylist, d):
    size = len(mylist)
    i = d
    while i < size:
        if mylist[i] < mylist[i - d]:
            tmp = mylist[i]
            j = i - d
            mylist[j + d] = mylist[j]
            j = j - d
            while j >= 0 and mylist[j] > tmp:
                mylist[j + d] = mylist[j]
                j = j - d
            mylist[j + d] = tmp
        i = i + d


def shell_sort(mylist):
    n = len(mylist)
    while n > 1:
        n = n // 3 + 1
        shell_pass(mylist, n)
    return mylist


# 直接选择排序
def select_sort(my_list):
    count = len(my_list) - 1
    for i in range(count):
        min_index = i
        for j in range(i + 1, count):
            if my_list[j] < my_list[min_index]:
                min_index = j
        my_list[i], my_list[min_index] = my_list[min_index], my_list[i]
    return my_list


# 冒泡排序
def bubble_sort(my_list):
    count = len(my_list) - 1
    while count >= 0:
        for i in range(count):
            if my_list[i] > my_list[i + 1]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
        count -= 1
    return my_list


# 快速排序
import sys

sys.setrecursionlimit(1000000)


def fast_sort(my_list):
    return quick_sort(my_list, 0, len(my_list) - 1)


def quick_sort(my_list, i, j):
    begin = i
    end = j
    if i >= j:
        return my_list
    key = my_list[j]
    while i < j:
        while i < j and my_list[i] <= key:
            i += 1
        my_list[j] = my_list[i]
        while i < j and my_list[j] >= key:
            j -= 1
        my_list[i] = my_list[j]
    my_list[i] = key
    quick_sort(my_list, begin, j - 1)
    quick_sort(my_list, i + 1, end)
    return my_list


# 堆排序
def heapify(lst, heapsize, root):
    leaf_left = root * 2 + 1
    leaf_right = leaf_left + 1
    large = root
    if leaf_left < heapsize and lst[leaf_left] > lst[large]:
        large = leaf_left
    if leaf_right < heapsize and lst[leaf_right] > lst[large]:
        large = leaf_right
    if large != root:
        lst[root], lst[large] = lst[large], lst[root]
        heapify(lst, heapsize, large)


def heap_sort(lst):
    for i in range((len(lst) - 1 - 1) / 2, -1, -1):
        heapify(lst, len(lst), i)
    for j in range(len(lst) - 1, -1, -1):
        lst[0], lst[j] = lst[j], lst[0]
        heapify(lst, j, 0)
    return lst


# 并归排序
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    num = len(lst) / 2
    right_l = merge_sort(lst[:num])
    left_l = merge_sort(lst[num:])
    return merge(left_l, right_l)



def merge(left, right):
    r, l = 0, 0
    reslut = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            reslut.append(left[l])
            l += 1
        else:
            reslut.append(right[r])
            r += 1
    reslut += right[r:]
    reslut += left[l:]
    return reslut

# 基数排序
import math

def radix_sort(a, radix=10):
    """a为整数列表， radix为基数"""
    K = int(math.ceil(math.log(max(a), radix))) # 用K位数可表示任意整数
    bucket = [[] for i in range(radix)]
    for i in range(1, K+1): # K次循环
        for val in a:
            bucket[val%(radix**i)/(radix**(i-1))].append(val) # 析取整数第K位数字 （从低到高）
        del a[:]
        for each in bucket:
            a.extend(each) # 桶合并
        bucket = [[] for i in range(radix)]
    return a


l = [1, 4, 3, 2, 5, 3, 5, 9, 5, 7]

print radix_sort(l)

import time


def test_sort(l, f):
    begin = time.time()
    res = f(l)
    # print "res:", res
    print "time.cost:", (time.time() - begin) * 1000


import random

length = 5000
a1 = range(0, length, 1)
a2 = range(length, 0, -1)
a3 = [random.randint(0, length) for i in range(length)]
a4 = [random.randint(0, length) for i in range(length)]
a5 = [random.randint(0, length) for i in range(length)]

# random.shuffle(range(length))
print "data.inited"

test_sort(a1, fast_sort)

print "=" * 10
test_sort(a2, fast_sort)

print "=" * 10
test_sort(a3, fast_sort)
print "=" * 10
test_sort(a4, fast_sort)
test_sort(a5, fast_sort)