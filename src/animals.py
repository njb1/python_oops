class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        raise NotImplementedError("Subclasses must implement this method")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Dog")

    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Cat")

    def make_sound(self):
        return "Meow!"
    
def get_animal_info(animal):
    return f"{animal.name} is a {animal.species} and says {animal.make_sound()}"

if __name__ == "__main__":
    dog = Dog("Buddy")
    cat = Cat("Whiskers")
    
    print(get_animal_info(dog))
    print(get_animal_info(cat))