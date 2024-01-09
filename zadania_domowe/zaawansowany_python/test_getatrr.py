'''
10. Przetestuj działanie getattr i wpływ atrybutów instancji/klasy oraz deskryptorów na jego działanie.
'''


class SomeClass:
    x = 10
    y = 20

    def __init__(self):
        self.z = 'instance attribute'


c = SomeClass()
x = getattr(c, 'x')
z = getattr(c, 'z')

print(x)
print(z)


class Descriptor:

    def __init__(self):
        self.x = "Descriptor attribute"

    def __get__(self, obj, objtype):
        return self.x

    def __set__(self, instance, value):
        self.x = value


class MyClass:
    x = Descriptor()


m = MyClass()
print(getattr(m, 'x'))
