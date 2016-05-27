# -*- coding:utf-8 -*-
__author__ = 'legenove'


class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree(object):
    def __init__(self, root):
        if root is None:
            self._root = None
        else:
            self._root = Node(root)

    def node_eq(self, other):
        if other is None:
            return False
        return self.root == other.root

    def __str__(self):
        m_list = []
        result = ""
        tree = self
        if tree.root is None:
            return result
        while True:
            result += tree.root
            if tree.left is not None:
                m_list.append(tree.left)
            if tree.right is not None:
                m_list.append(tree.right)
            if m_list:
                tree = m_list.pop(0)
            else:
                break
        return result

    def is_leaf(self):
        return (self._root.left is None) and (self._root.right is None)

    @property
    def left(self):
        return self._root.left

    @left.setter
    def left(self, obj):
        self._root.left = obj

    @property
    def right(self):
        return self._root.right

    @right.setter
    def right(self, obj):
        self._root.right = obj

    @property
    def root(self):
        return self._root.data

    @root.setter
    def root(self, value):
        if value is None:
            self._root = None
        else:
            self._root = Node(value)


def pre_order(tree):
    result = ""
    if tree.root is None:
        return result
    result += tree.root
    if tree.left is not None:
        result += pre_order(tree.left)
    if tree.right is not None:
        result += pre_order(tree.right)
    return result


def in_order(tree):
    result = ""
    if tree.root is None:
        return result
    if tree.left is not None:
        result += in_order(tree.left)
    result += tree.root
    if tree.right is not None:
        result += in_order(tree.right)
    return result


def post_order(tree):
    result = ""
    if tree.root is None:
        return result
    if tree.left is not None:
        result += post_order(tree.left)
    if tree.right is not None:
        result += post_order(tree.right)
    result += tree.root
    return result


def print_tree(tree):
    m_list = []
    result = ""
    if tree.root is None:
        return result
    while True:
        result += tree.root
        if tree.left is not None:
            m_list.append(tree.left)
        if tree.right is not None:
            m_list.append(tree.right)
        if m_list:
            tree = m_list.pop(0)
        else:
            break
    return result


def get_depth(tree):
    if tree is None or tree.root == None:
        return 0
    left_depth = get_depth(tree.left)
    right_depth = get_depth(tree.right)
    return (left_depth > right_depth and [left_depth] or [right_depth])[0] + 1


def is_balance_tree(tree):
    if tree is None or tree.root == None:
        return True
    if abs(get_depth(tree.left) - get_depth(tree.right)) > 1:
        return False
    else:
        return is_balance_tree(tree.left) and is_balance_tree(tree.right)


def get_pos(tree, node, pos):
    if tree is None or tree.root is None:
        return False, 0
    if node.node_eq(tree):
        return True, pos
    flag, _pos = get_pos(tree.left, node, pos * 2)
    if flag:
        return flag, _pos
    else:
        return get_pos(tree.right, node, pos * 2 + 1)


def get_binary_size(pos):
    length = 0
    while pos != 0:
        pos /= 2
        length += 1
    return length


def find_parent_position(tree, node1, node2):
    f1, pos1 = get_pos(tree, node1, 1)
    f2, pos2 = get_pos(tree, node2, 1)
    if pos1 == pos2:
        return pos1
    less = get_binary_size(pos1) - get_binary_size(pos2)
    while less > 0:
        pos1 /= 2
        less -= 1
    while less < 0:
        pos2 /= 2
        less += 1
    while pos1 != pos2:
        pos1 /= 2
        pos2 /= 2
    return pos1


r = BinaryTree("a")
r.left = BinaryTree("b")
r.right = BinaryTree("c")
r.left.right = BinaryTree("d")
r.right.left = BinaryTree("e")
r.right.right = BinaryTree("f")
r.right.right.left = BinaryTree("g")
r1 = BinaryTree("f")
r3 = BinaryTree("g")

r2 = BinaryTree("d")
print pre_order(r)
print in_order(r)
print post_order(r)

print print_tree(r)

print is_balance_tree(r)

print r.right == r1

print find_parent_position(r, r3, r1)