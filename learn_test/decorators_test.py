def dec(fun, a, b):
    def _f(f):
        def warp(*args, **kwargs):
            print "1"
            if fun(a, b):
                return f(*args, **kwargs)
            else:
                return
        return warp

    return _f


def dec_out(a, b):
    def f(a, b):
        return True if a < b else False

    return dec(f, a, b)


@dec_out(4, 3)
def foo(a):
    print a


def foo1(a):
    print a


foo(2)
dec_out(3, 4)(foo1)(2)