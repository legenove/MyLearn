# -*- coding:utf-8 -*-
__author__ = 'legenove'


def binary_search(a_list, item):
    found = False
    frist = 0
    last = len(a_list) - 1
    while frist <= last and not found:
        middle = (frist + last) // 2
        if a_list[middle] == item:
            found = True
        elif a_list[middle] > item:
            last = middle - 1
        else:
            frist = middle + 1
    return found


def binary_recursion_search(a_list, item):
    if a_list == []:
        return False
    else:
        middle = len(a_list) // 2
        if item == a_list[middle]:
            return True
        else:
            if item < a_list[middle]:
                return binary_recursion_search(a_list[:middle], item)
            else:
                return binary_recursion_search(a_list[middle:], item)


print binary_recursion_search(range(10), 6)