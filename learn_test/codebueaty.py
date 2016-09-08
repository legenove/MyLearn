# -*- coding: utf-8 -*-
__author__ = 'legenove'


def count2(v):
    num = 0
    while (v):
        num += (v & 0x01)
        v = v >> 1
    return num


print count2(15)


def gcd(m, n):
    while m % n != 0:
        m, n = n, m % n
    return n


print gcd(3, 6)


def heapify(lst, lst_size, root):
    left = root * 2 + 1
    right = left + 1
    large = root
    if left < lst_size and lst[left] > lst[large]:
        large = left
    if right < lst_size and lst[right] > lst[large]:
        large = right
    if large != root:
        lst[large], lst[root] = lst[root], lst[large]
        heapify(lst, lst_size, large)

# def static_fun(f):
#     def fun(*args,**kwargs):
#         if __name__ == '__main__':
#             f(*args,**kwargs)
#         else:
#             raise ImportError('can not use static function')
#     return fun
#
# @static_fun
# def _like():
#     print 'like'
# _like()
#
# def __like():
#     print 'like'


def max_k(lst, k):
    num = len(lst)
    for i in range((num - 2) / 2, -1, -1):
        heapify(lst, num, i)
    for i in range(num - 1, num - 1 - k, -1):
        lst[0], lst[i] = lst[i], lst[0]
        print lst[i]
        heapify(lst, i, 0)
    return lst

print max_k([13, 62, 75, 37, 35, 02, 52, 35, 69, 73, 92, 32, 47, 3], 6)



__all__ = []