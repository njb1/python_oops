class Greeter:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    
    def _full_name(self):
        full_name = self.firstname + " " + self.lastname
        return full_name

    def greet(self):
        # print(f"Good evening {self._full_name()}, how are you today?")
        return f"Good evening {self._full_name()}, how are you today?"


if __name__ == "__main__":
    greet_person = Greeter("Bob", "Marley")
    print(greet_person.greet())