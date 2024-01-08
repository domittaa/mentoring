'''
2. Zaimplementuj metaklase, która weryfikować będzie, czy klasa implementuje odpowiednie atrybuty i metody,
 oraz ich typy. np. metodę hello_world i atrybut MESSAGE.
'''


class VerifyMeta(type):
    def __init__(cls, name, bases, dct):
        func = dct.get('hello_world', None)
        attr = dct.get('MESSAGE', None)
        if func and attr and isinstance(attr, str):
            print(f"Class {cls} passed verification")
        else:
            print(f"Class {cls} did not pass verification")


class A(metaclass=VerifyMeta):
    MESSAGE = "Some message"

    def hello_world(self):
        pass


class B(metaclass=VerifyMeta):
    pass


class C(metaclass=VerifyMeta):
    MESSAGE = 56

    def hello_world(self):
        pass

