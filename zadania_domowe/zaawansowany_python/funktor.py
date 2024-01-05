'''
3. Zaimplementuj funktor zliczający liczbę wywołań.
'''


class Counter:
    TOTAL_COUNT = 0

    def __call__(self):
        self.TOTAL_COUNT += 1


class Caller:
    def __init__(self):
        self.caller = Counter()
