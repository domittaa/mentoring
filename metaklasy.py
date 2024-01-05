def func(self):
    print(f"Func called for {self}")


# Define the metaclass
class GreetingMeta(type):
    def __new__(cls, name, bases, dct):
        # Add a new method to the class
        print(dct)
        lam = lambda self: f"Hello from {self.__class__}"
        print(lam)
        dct['greet'] = lam
        dct['func'] = func
        return super(GreetingMeta, cls).__new__(cls, name, bases, dct)

# Use the metaclass to create a new class
class MyClass(metaclass=GreetingMeta):
    def foo(self):
        ...

# Another class using the metaclass
class AnotherClass(metaclass=GreetingMeta):
    pass

# Example usage
obj1 = MyClass()
obj2 = AnotherClass()

print(obj1.func())
print(obj1.func)
print(obj1.greet)
print(obj1.greet())  # Prints: Hello from MyClass
print(obj2.greet())  # Prints: Hello from AnotherClass