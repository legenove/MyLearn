# -*- coding:utf-8 -*-
__author__ = 'legenove'

import math

# 直接插入排序 o(n) o(n^2) o(n^2) o(1)
def insert_sort(l):
    pass


# 直接选择排序
def select_sort(my_list):
    pass


# 冒泡排序
def bubble_sort(my_list):
    pass


# 快速排序
def fast_sort(my_list):
    pass


# 堆排序
def heap_sort(my_list):
    def heapify(my_l, heapsize, i):
        if i >= heapsize:
            return
        root = i
        left = root * 2 + 1
        right = left + 1
        large = root
        while left < heapsize and my_l[large] < my_l[left]:
            large = left
        while right < heapsize and my_l[large] < my_l[right]:
            large = right
        if large != root:
            my_l[large], my_l[root] = my_l[root], my_l[large]
            heapify(my_l, heapsize, large)

    for i in range((len(my_list) - 2) / 2, -1, -1):
        heapify(my_list, len(my_list), i)
    for j in range(len(my_list) - 1, -1, -1):
        my_list[0], my_list[j] = my_list[j], my_list[0]
        heapify(my_list, j, 0)
    return my_list


# 并归排序
def merge_sort(my_list):
    pass


# 基数排序
def radix_sort(my_list, radix=10):
    pass


# 希尔排序
def shell_sort(my_list):
    pass


l = [4, 1, 3, 2, 5, 3, 5, 9, 5, 7]
l1 = [4, 1, 3, 2, 5, 3, 5, 9, 5, 7]
print sorted(l1)
print heap_sort(l)