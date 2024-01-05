from abc import ABC, abstractmethod
from typing import Protocol


class IAnimal(Protocol):
    LEGS_NUMBER: int

    def make_sound(self):
        ...


class AbstractAnimal(ABC):

    @abstractmethod
    def make_sound(self):
        ...


class Duck:
    LEGS_NUMBER = 5

    def make_sound(self):
        print("Kwa kwa")


class Chicken(AbstractAnimal):
    def make_sound(self):
        print("Ko ko ko")


def check_proto_animal(animal: IAnimal):
    animal.make_sound()


def check_abc_animal(animal: AbstractAnimal):
    animal.make_sound()


check_proto_animal(Duck())
check_abc_animal(Chicken())