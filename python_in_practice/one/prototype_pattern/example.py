import sys
import copy
class Point:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


def make_object(Class, *args, **kwargs):
    return Class(*args, **kwargs)


point1 = Point(1, 2)
point2 = eval("{}({},{})".format('Point', 2, 3))
point3 = getattr(sys.modules[__name__], 'Point')(2,3)
point4 = globals()['Point'](3,4)
point5 = make_object(Point, 2,3)
point6 = copy.deepcopy(point1)
point6.x = 7
point6.y = 8

point7 = point6.__class__(5,6)
