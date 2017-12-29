# import signal
# # Define signal handler function
# def myHandler(signum, frame):
#     print('I received: ', signum)
#
# # register signal.SIGTSTP's handler
# signal.signal(signal.SIGTSTP, myHandler)
# signal.pause()
# print('End of Signal Demo')
#
from blinker import Namespace

_signal = Namespace()

abc = _signal.signal('abc')

@abc.connect()
def abc_reciver(sender,*kw):
    print 'aaaaa', sender