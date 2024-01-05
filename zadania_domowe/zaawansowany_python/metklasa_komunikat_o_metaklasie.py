'''
1. Zaimplementuj metaklase, która będzie wypisywać komunikat o aktualnie tworzonej klasie.'
'''


class NotifyMeta(type):
    def __init__(cls, name, bases, dct):
        print(f"{cls} is being created")


class A(metaclass=NotifyMeta):
    pass


class B(metaclass=NotifyMeta):
    pass
