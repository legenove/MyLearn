# -*- coding:utf-8 -*-
__author__ = 'legenove'


class BinaryTree(object):
    def __init__(self, root):
        self.key = root
        self.left = None
        self.right = None

    def insert_left(self, node):
        if self.left == None:
            self.left = BinaryTree(node)
        else:
            t = BinaryTree(node)
            t.left = self.left
            self.left = t

    def insert_right(self, node):
        if self.right == None:
            self.right = BinaryTree(node)
        else:
            t = BinaryTree(node)
            t.right = self.right
            self.right = t

    def get_right(self):
        return self.right

    def get_left(self):
        return self.left

    def set_root(self, obj):
        self.key = obj

    def get_root(self):
        return self.key


class BinarySearchTree(object):
    def __init__(self, key):
        self.root = key
        self.left = None
        self.right = None



def insert_bst(t, key):
    if t is None:
        t = BinarySearchTree(key)
    else:
        if t.root < key: #插入右子树
            t.right = insert_bst(t.right, key)

        elif t.root > key: #插入左子树
            t.left = insert_bst(t.left, key)

    return t


def find_min(t):
    if t.left:
        return find_min(t.left)
    else:
        return t


def find_key(t, key):
    if t is None:
        return 0
    else:
        if t.root < key:
            return find_key(t.right, key)
        elif t.root > key:
            return find_key(t.left, key)
        else:
            return 1


def del_key(t, key):
    if t is None:
        return t
    if t.root < key:
        t.right = del_key(t.right, key)
    elif t.root > key:
        t.left = del_key(t.left, key)
    else:
        if t.right and t.left:
            tmp = find_min(t.right)
            t.root = tmp.root
            del_key(t.right, tmp.root)
        elif t.right is None:
            t = t.left
        elif t.left is None:
            t = t.right
    return t


t = None
t = insert_bst(t, 3)
t = insert_bst(t, 1)
t = insert_bst(t, 5)
t = insert_bst(t, 4)
t = insert_bst(t, 6)
t = insert_bst(t, 2)

print t
print find_min(t)
print find_key(t, 2)
t = del_key(t, 5)
print t
