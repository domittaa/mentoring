'''
3. Zaimplementuj funktor zliczający liczbę wywołań.
'''


class Counter:
    TOTAL_COUNT = 0

    def __call__(self):
        self.TOTAL_COUNT += 1

    def get_call_count(self):
        return self.TOTAL_COUNT


functor = Counter()
functor()
functor()
print(functor.get_call_count())


class FunctionCounter:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.func(*args, *kwargs)


def func():
    pass


counter = FunctionCounter(func)
counter()
counter()
print(counter.count)
