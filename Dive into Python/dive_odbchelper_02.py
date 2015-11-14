# -*- coding:utf-8 -*-
__author__ = 'legenove'

'''
    01、函数声明要用小写,build_connection_string
    02、""" doc string  func.__doc__
    03、测试模块 if __name__ == "__main__":
    04、格式化字符串 "%s=%s" % (k, v)
    05、list comprehension 列表推到 ["%s=%s" % (k, v) for k, v in params.items()]
    06、.join() 方法
'''


def build_connection_string(params):
    """
    Build a connection string from a dictionary of parameters
    :param params:
    :return: string
    """
    return ";".join(["%s=%s" % (k, v) for k, v in params.items()])

if __name__ == "__main__":
    myParams = {
        "server": "mpilgrim",
        "database": "master",
        "uid": "sa",
        "pwd": "secret",
    }
    print build_connection_string(myParams)
    print build_connection_string.__doc__