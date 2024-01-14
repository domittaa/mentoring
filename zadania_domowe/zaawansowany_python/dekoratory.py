'''
4. Zaimplementuj odpowiedniki dekoratorów: staticmethod, classmethod, property i cache.
'''


class StaticMethod:
    def __init__(self, f):
        self.f = f

# obj.method(*args) -> method(*args)
    def __get__(self, obj, objtype=None):
        return self.f

    def __set__(self, *args, **kwargs):
        return self.f(*args, **kwargs)


class ClassMethod:
    def __init__(self, f):
        self.f = f

#  obj.method(type(obj), *args) -> method(type(obj), *args).
    def __get__(self, obj, objtype=None):
        if objtype is None:
            objtype = type(obj)

        def func(*args):
            return self.f(objtype, *args)
        return func


class Property:
    def __init__(self, f):
        self.f = f

    def __get__(self, obj, objtype=None):
       pass

    def __set__(self, *args, **kwargs):
        pass

    def __delete__(self, instance):
        pass


class Cache:
    def __init__(self, f):
        self.f = f
        self.cache = {}

    def __get__(self, obj, objtype=None):
        if obj in self.cache:
            return self.cache[obj]
        result = self.f(obj)
        self.cache[obj] = result
        return result
