'''
1. Zaimplementuj metaklase, która będzie wypisywać komunikat o aktualnie tworzonej klasie.'
'''


class NotifyMeta(type):
    def __new__(cls, *args, **kwargs):
        print(f"{cls.__name__} is being created")
        return super().__new__(cls, *args, **kwargs)


class A(metaclass=NotifyMeta):
    pass


class B(metaclass=NotifyMeta):
    pass

