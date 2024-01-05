class Point:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y

print(dir(Point(1,1)))
print(Point(1,1).__slots__)

#  following lines will throw errors
Point(1,2).z = "error..."
print(Point(1,1).__dict__)