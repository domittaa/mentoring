'''
2. Zaimplementuj metaklase, która weryfikować będzie, czy klasa implementuje odpowiednie atrybuty i metody,
 oraz ich typy. np. metodę hello_world i atrybut MESSAGE.
'''


class VerifyMeta(type):
    def __init__(cls, name, bases, dct):
        try:
            dct['hello_world'] and dct['MESSAGE']
        except KeyError:
            print(f"Class {cls} did not pass verification")
        else:
            print(f"Class {cls} passed verification")


class A(metaclass=VerifyMeta):
    MESSAGE = "Some message"

    def hello_world(self):
        pass


class B(metaclass=VerifyMeta):
    pass

