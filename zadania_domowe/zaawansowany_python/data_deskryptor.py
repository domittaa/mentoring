'''
8. Zaimplementuj data deskryptor, który będzie realizować funkcję validatora,
czyli będzie weryfikować, czy ustawiona wartość jest zgodna z regułami podanymi podczas jego inicjalizacji.
'''


class DataDescriptorValidator:
    def __init__(self, x):
        self.x = x
        if self.x < 0:
            raise Exception("Value cannot be lower than 0")
        elif self.x > 100:
            raise Exception("Value cannot be higher than 100")

    def __get__(self, obj, type):
        print("Getting the x value..")
        return self.x

    def __set__(self, obj, val):
        if val < 0:
            raise Exception("Value cannot be lower than 0")
        elif val > 100:
            raise Exception("Value cannot be higher than 100")
        else:
            print(f"Setting the value to {val}")
            self.x = val


class MyClass:
    obj = DataDescriptorValidator(5)


m = MyClass()
print(m.obj)
m.obj = 120
