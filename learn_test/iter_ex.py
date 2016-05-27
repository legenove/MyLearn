# -*- coding: utf-8 -*-

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]

print L2


def triangles():
    def _yanghui_trangle(n, result):
        if n == 1:
            return [1]
        else:
            return [sum(i) for i in zip([0] + result, result + [0])]

    m = 1
    r = [1]
    while True:
        r = _yanghui_trangle(m, r)
        yield r
        m += 1

n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break


