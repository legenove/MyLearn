import sys
import importlib

class Loader():

    module = None
    name = None

    def find_module(self, name, path):
        self.name = name
        sys.meta_path.remove(self)
        self.module = importlib.import_module(name)
        sys.meta_path.insert(0, self)
        return self

    def load_module(self, name):
        if not self.module:
            raise ImportError("Unable to load module:"+name)

        return self.module

sys.meta_path.insert(0, Loader())

from a import *
import httplib
import b
A()