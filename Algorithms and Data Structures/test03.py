# -*- coding:utf-8 -*-
__author__ = 'legenove'


class Stack(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []


class Deque(object):
    def __init__(self):
        self.items = []

    def add_rear(self, item):
        self.items.insert(0, item)

    def add_front(self, item):
        self.items.append(item)

    def remove_rear(self):
        return self.items.pop(0)

    def remove_front(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)


# Completed extended par_checker for: [,{,(,),},]
def par_checker(symbol_string):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index += 1
    if s.is_empty() and balanced:
        return True
    else:
        return False


def matches(o, c):
    opens = '([{'
    closes = ')]}'
    return opens.index(o) == closes.index(c)


print par_checker('(())')
print par_checker('([{])})')
print par_checker('([{}])')