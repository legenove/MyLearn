# -*- coding: utf-8 -*-


class Key(unicode):
    def __getitem__(self, key):
        if self:
            return Key(u"%s:%s" % (self, key))
        else:
            return Key(u"%s" % key)


class BaseClass(type):
    _attributes = {}

    def __init__(cls, name, bases, attrs):
        print name
        print bases
        for parent in bases:
            if not isinstance(parent, BaseClass):
                continue
            print parent, 11111
            for k, v in parent._attributes.iteritems():
                print k, v, 2222
        print attrs
        super(BaseClass, cls).__init__(name, bases, attrs)


class A(object):
    __metaclass__ = BaseClass
    d = 'd'

    def __init__(self, **kwargs):
        self.update_attributes(**kwargs)

    @property
    def attributes(self):
        """Return the attributes of the model.
        Returns a dict with models attribute name as keys
        and attribute descriptors as values.
        """
        return dict(self._attributes)

    def update_attributes(self, **kwargs):
        attrs = self.attributes.values()
        for att in attrs:
            if att.name in kwargs:
                att.__set__(self, kwargs[att.name])


class B(A):
    pass


a = A(a=1)
# b = B(1)