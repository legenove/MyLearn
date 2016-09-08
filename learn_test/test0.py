__author__ = 'legenove'

import random

# a = [0, 1, 2]
# print a[random.randint(0, len(a)) - 1]
# print a[random.randint(0, len(a)) - 1]
# print a[random.randint(0, len(a)) - 1]


from codebueaty import max_k
max_k([13, 62, 75, 37, 35, 02, 52, 35, 69, 73, 92, 32, 47, 3], 6)


# FooChild = type('FooChild', (Foo,), {'echo_bar': echo_bar})

class B(type):
    def __new__(cls, *args):
        print('B __new')
        return super(B, cls).__new__(cls, *args)


class A(object):
    __metaclass__ = B

    def __new__(cls, *args):
        print 'A __new'
        return object.__new__(cls, *args)


a = A()