# -*- coding: utf-8 -*-
__author__ = 'legenove'

print "*******************************"
print "高阶函数 map() reduce() filter() sorted()"
print "*******************************"


def add(x, y, fun):
    return fun(x) + fun(y)


print add(2, -3, abs)


def f(x):
    return x * x


r = map(f, range(10))

print list(r)

print list(map(str, range(10)))

print sum(range(10))


def fn(x, y):
    return x * 10 + y


print reduce(fn, range(1, 5))

print reduce(lambda x, y: x * 10 + y, range(1, 5))

L1 = ['adam', 'LISA', 'barT']
print map(lambda x: x.capitalize(), L1)
print map(str.title, L1)
# TODO map different
print "py2:map返回list   py3:map返回一个Iterator"


def prod(l):
    return reduce(lambda x, y: x * y, l)


print prod([3, 5, 4, 2, 6])


def is_primes(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True


print filter(is_primes, range(1, 100))


def is_palindrome(n):
    return str(n) == str(n)[::-1]


print filter(is_palindrome, range(1, 1000))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[1]


print sorted(L, cmp=None, key=by_name, reverse=True)


def log(func):
    def wapper(*args, **kwargs):
        print "begin call"
        func(*args, **kwargs)
        print "end call"

    return wapper


@log
def now():
    print "100099"


now()


def log(text):
    def _f(func):
        def wapper(*args, **kwargs):
            print "begin call %s" % text
            func(*args, **kwargs)
            print "end call"

        return wapper

    return _f


@log("now")
def now():
    print "100099"


now()