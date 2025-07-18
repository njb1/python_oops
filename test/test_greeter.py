from src.greeter import Greeter

def test_greeter_full_name():
    test_greeter = Greeter("Neil", "Burns")
    assert test_greeter._full_name() == "Neil Burns"


def test_greeter_greet():
    test_greeter = Greeter("Bob", "Marley")
    assert test_greeter.greet() == "Good evening Bob Marley, how are you today?"