__author__ = 'legenove'


class abc(object):
    def a(self, a1):
        print a1

    @classmethod
    def b(cls):
        cls.a(cls, 1)


abc.b()