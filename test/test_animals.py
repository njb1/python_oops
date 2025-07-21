import pytest
from src.animals import Animal, Dog, Cat

def test_animal_creation():
    dog = Dog("Buddy")
    assert dog.name == "Buddy"
    assert dog.species == "Dog"
    assert dog.make_sound() == "Woof!"

    cat = Cat("Whiskers")
    assert cat.name == "Whiskers"
    assert cat.species == "Cat"
    assert cat.make_sound() == "Meow!"