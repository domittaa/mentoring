class Functor:
    __COUNTER = 0

    def get_call_count(self):
        return self.__COUNTER

    def __call__(self, *args, **kwargs):
        self.__COUNTER += 1
        print("Hello World!!!")


class FunctorMethod:
    def __init__(self, caller):
        self.caller = caller

    @staticmethod
    def __func_body(self, x,y):
        print(f"Caller self: {self}")
        return x+y

    def __call__(self, x, y):
        return self.__func_body(self.caller, x, y)


class Foo:
    def trolo(self):
        ...


obj = Foo()
obj.add = FunctorMethod(obj)


my_func = Functor()
my_func()
my_func()
print(my_func.get_call_count())

print(obj.add(1,2))

print(obj.trolo)
print(Foo.trolo)