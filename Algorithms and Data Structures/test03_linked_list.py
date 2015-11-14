# -*- coding:utf-8 -*-
__author__ = 'legenove'


class Node(object):
    def __init__(self, item):
        self.data = item
        self.next = None

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def get_next(self):
        return self.next

    def set_next(self, next_node):
        self.next = next_node


class UnorderedList(object):
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        node = Node(item)
        node.next = self.head
        self.head = node

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if found:
            if previous is None:
                self.head = current.get_next()
                current.set_next(None)
            else:
                previous.set_next(current.get_next())
                current.set_next(None)
            return 1
        return 0

    def search(self, item):
        found = False
        current = self.head
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.get_next()
        return count
    
if __name__ == "__main__":
    myList = UnorderedList()
    print myList.is_empty()
    myList.add(31)
    myList.add(77)
    myList.add(17)
    myList.add(93)
    myList.add(26)
    myList.add(54)
    print myList.size()
    print myList.search(17)
    print myList.remove(17)
    print myList.is_empty()
    print myList.search(17)
    print myList.size()