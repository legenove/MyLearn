import unittest


class Widget(object):
    x = 50
    y = 50

    def __init__(self, name):
        self.name = name

    def size(self):
        return (self.x, self.y)

    def resize(self, x, y):
        self.x, self.y = x, y

    def dispose(self):
        del self


class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        print('start', self.__doc__)
        self.widget = Widget('The widget')

    def test_default_widget_size(self):
        self.assertEqual(self.widget.size(), (50, 50),
                         'incorrect default size')

    def test_widget_resize(self):
        self.widget.resize(100, 100)
        self.assertEqual(self.widget.size(), (100, 100),
                         'wrong size after resize')

    def tearDown(self):
        self.widget.dispose()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase('test_default_widget_size'))
    suite.addTest(WidgetTestCase('test_widget_resize'))
    print suite.countTestCases()
    return suite

if __name__ == '__main__':
    # suite()
    runner = unittest.TextTestRunner()
    runner.run(suite())