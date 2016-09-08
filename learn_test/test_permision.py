
class PermissionDenied(Exception):
    """The user did not have permission to do that"""
    pass

def authenticate(*args,**kwargs):
    try:
        raise PermissionDenied(u'abc')
    except PermissionDenied,e:
        return e

class ABC(object):
    def __init__(self):
        self.user_cache = None
    def abc(self):
        self.user_cache = authenticate(username='1',
                               password='1')
        if isinstance(self.user_cache, PermissionDenied):
            e = self.user_cache
            self.user_cache = None
            pass

a = ABC()
a.abc()