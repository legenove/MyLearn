__author__ = 'legenove'
from blinker import Namespace

_signal = Namespace()

abc = _signal.signal('abc')
abc.send('111')


