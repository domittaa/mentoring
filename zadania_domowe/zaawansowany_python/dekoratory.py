'''
4. Zaimplementuj odpowiedniki dekoratorów: staticmethod, classmethod, property i cache.
'''


class StaticMethod:
    def __init__(self, f):
        self.f = f

    def __get__(self, obj, objtype=None):
        return self.f

    def __set__(self, *args, **kwargs):
        return self.f(*args, **kwargs)


class ClassMethod:
    def __init__(self, f):
        self.f = f

    def __get__(self, obj, objtype=None):
        pass


class Property:
    def __init__(self, f):
        self.f = f

    def __get__(self, obj, objtype=None):
       pass

    def __set__(self, *args, **kwargs):
        pass


class Cache:
    def __get__(self, obj, objtype=None):
        pass

    def __set__(self, *args, **kwargs):
        pass
