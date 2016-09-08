import os, sys
import glob

# File : builtin-apply-example-1.py


def function(a, b):
    print a, b


apply(function, (1, 2))
apply(function, (1,), {'b': 2})
apply(function, (), {'a': 1, 'b': 2})


class Rectangle(object):
    Tag = "Rectangle"

    def __init__(self, color="white", width=10, height=10):
        print "create a ", color, self, "sized", width, "x", height

    def __str__(self):
        return self.Tag


class RoundedRectangle(Rectangle):
    Tag = "RoundedRectangle"

    def __init__(self, **kwargs):
        apply(Rectangle.__init__, (self,), kwargs)


rect = Rectangle(color="green", height=100, width=100)
rect = RoundedRectangle(color='bule', height=20)

modules = []

for module_file in glob.glob("*-plugin.py"):
    try:
        module_name, ext = os.path.splitext(os.path.basename(module_file))
        module = __import__(module_name)
        modules.append(module)
    except ImportError:
        pass

for module in modules:
    if hasattr(module, 'hello'):
        # print repr(getattr(module, 'hello'))
        if callable(getattr(module, 'hello')):
            getattr(module, 'hello')()


class LazyImport(object):
    def __init__(self, module_name):
        self.module_name = module_name
        self.module = None

    def __getattr__(self, item):
        if self.module is None:
            module_name, ext = os.path.splitext(os.path.basename(self.module_name))
            self.module = __import__(module_name)
        return getattr(self.module, item)


plugin = LazyImport("1-plugin.py")

print isinstance(plugin, LazyImport)
print plugin.hello


def dump(value):
    # print value, "=>", dir(value)
    print type(value), value


dump(0)
dump(1.0)
dump(0.0j)  # complex number
dump([])  # list
dump({})  # dictionary
dump("string")  # string
dump(len)  # function
dump(sys)  # module


def load(file):
    if isinstance(file, type("")):
        file = open(file, "rb")
    return file.read()


print len(load("1-plugin.py"))

a = compile("print 'assfdsa'", "", "exec")
exec a