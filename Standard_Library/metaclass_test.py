__author__ = 'legenove'


class ObjectCreator(object):
    def _test(self):
        print 'test'


class Abc(object):
    pass


a = ObjectCreator()

print ObjectCreator
print a
print a._test()

print hasattr(ObjectCreator, 'abc')
setattr(ObjectCreator, 'abc', Abc())
print hasattr(ObjectCreator, 'abc')
print ObjectCreator.abc
ObjectCreator.abc = Abc()
print hasattr(ObjectCreator, 'abc')
print ObjectCreator.abc

Foo = type('Foo', (), {'bar': True})


def echo_bar(self):
    print self.bar


FooChild = type('FooChild', (Foo,), {'echo_bar': echo_bar})



