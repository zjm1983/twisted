class A:
    def a(self):
        return 'b'


class B(A, object):
    def b(self):
        return 'c'


class Inherit(A):
    def a(self):
        return 'd'
