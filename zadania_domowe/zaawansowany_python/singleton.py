'''
6. Zaimplementuj wzorzec Singleton oparty na metaklasie.
'''


class MetaSingleton(type):
    INSTANCES = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.INSTANCES:
            cls.INSTANCES[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls.INSTANCES[cls]


class Singleton(metaclass=MetaSingleton):
    pass


a = Singleton()
b = Singleton()
c = Singleton()
print(a)
print(b)
print(c)
print(a is b)
print(b is c)



