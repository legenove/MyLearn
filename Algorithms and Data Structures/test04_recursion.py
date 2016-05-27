# -*- coding:utf-8 -*-
__author__ = 'legenove'

import turtle


def draw_spiral(my_turtle, line_len):
    if line_len > 0:
        my_turtle.forward(line_len)
        my_turtle.right(90)
        draw_spiral(my_turtle, line_len - 5)


def tree(branch_len, t):
    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        tree(branch_len - 15, t)
        t.left(40)
        tree(branch_len - 15, t)
        t.right(20)
        t.backward(branch_len)


def main():
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75, t)
    my_win.exitonclick()


def move(n, A, B):
    print "move:", n, " from ", A, " to ", B


def hanoi(n, A, B, C):
    if n <= 1:
        move(n, A, C)
    else:
        hanoi(n - 1, A, C, B)
        move(n, A, C)
        hanoi(n - 1, B, A, C)


hanoi(4, "A", 'B', 'C')