class RevealAccess:
    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        print(f"Retrieving {self.name}")
        return self.val

    def __set__(self, obj, val):
        print(f"Updating {self.name} to {val}")
        self.val = val

class MyClass:
    x = RevealAccess(10, 'variable "x"')


# Example usage
m = MyClass()
print(m.x)
m.x = 20