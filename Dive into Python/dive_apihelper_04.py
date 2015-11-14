# -*- coding:utf-8 -*-
__author__ = 'legenove'

'''
    1、dir() 返回方法名
    2、callable 表示可调用的，返回True；否则返回False
    3、getattr 可得到一个直到运行时才知道名称函数的引用
    4、list comprehension 的过滤列表 [method for method in dir(object) if callable(getattr(object, method))]
        if 语句的使用，过滤了一些结果。
    5、and 和 or 返回结果。
        and 从左到右演算表达式的值，为假时，返回第一个假的值；否则返回最后一个真的值。
        or 从左到右演算表达式的值，为真时，返回第一个真的值；否则返回最后一个假的值。
    6、and-or 使用技巧 类似于C语言中的 bool ? a : b  下面有两种方法
        a> exper and a or b
            安全使用==> (exper and [a] or [b])[0]
            由于[a]一定为非空列表，当a = ""时，表达式不会受到影响
        b> a if exper else b
    7、匿名函数lambda  g = lambda x : x**2
'''


def info(object, spacing=10, collapse=1):
    """
    Print methods and doc strings.

    Takes module, class, list, dictionary,or string.
    :param object:
    :param spacing:
    :param collapse:
    :return: None
    """
    methodList = [method for method in dir(object) if callable(getattr(object, method))]

    processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)

    print "\n".join(["%s %s" %
                     (method.ljust(spacing), processFunc(str(getattr(object, method).__doc__)))
                     for method in methodList])


if __name__ == "__main__":
    import dive_odbchelper_02

    print info.__doc__
    li = [0, 1, 2, 3]
    info(dive_odbchelper_02, 40, 0)
    print getattr(li, 'pop')()

    import types

    object = dive_odbchelper_02
    method = "build_connection_string"

    print type(getattr(object, method)) == types.FunctionType
    print callable(getattr(object, method))

    # and 和 or

    # ##and 从左到右演算表达式的值，为假时，返回第一个假的值；否则返回最后一个真的值。
    print 'a' and 'b'  # return 'a'
    print '' and 'b'  # return ''
    print 'a' and 'b' and 'c'  # return 'c'

    # ##or 从左到右演算表达式的值，为真时，返回第一个真的值；否则返回最后一个假的值。
    print 'a' or 'b'  # return 'a'
    print '' or 'b'  # return 'b'
    print '' or [] or {}  # return {}
    print '' or '' or 'c'  # return 'c'