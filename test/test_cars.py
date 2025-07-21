import pytest
from src.cars import (
    Car,
)

def test_car_initialization():
    car = Car("Toyota", "Corolla", 2020)
    assert car.make == "Toyota"
    assert car.model == "Corolla"
    assert car.year == 2020

def test_set_make():
    car = Car("Toyota", "Corolla", 2020)
    car.set_make("Honda")
    assert car.get_make() == "Honda"

def test_set_model():
    car = Car("Toyota", "Corolla", 2020)
    car.set_model("Civic")
    assert car.get_model() == "Civic"

def test_set_year():
    car = Car("Toyota", "Corolla", 2020)
    car.set_year(2021)
    assert car.get_year() == 2021

def test_get_description():
    car = Car("Toyota", "Corolla", 2020)
    assert car.get_description() == "Year: 2020, Make: Toyota, Model Corolla"

def test_set_mileage():
    car = Car("Toyota", "Corolla", 2020)
    car.set_mileage(15000)
    assert car.get_mileage() == 15000

def test_set_color():
    car = Car("Toyota", "Corolla", 2020)
    car.set_color("Red")
    assert car.get_color() == "Red"

def test_set_engine_type():
    car = Car("Toyota", "Corolla", 2020)
    car.set_engine_type("electric")
    assert car.get_engine_type() == "electric"

def test_invalid_engine_type():
    car = Car("Toyota", "Corolla", 2020)
    with pytest.raises(ValueError):
        car.set_engine_type("hybrid")  # Invalid engine type