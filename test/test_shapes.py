import pytest
from src.shapes import (
    Rectangle,
    Shapes,
    Circle
)

def test_rectangle_area():
    rectangle = Rectangle(5, 10)
    assert rectangle.area() == 50

def test_rectangle_perimeter():
    rectangle = Rectangle(5, 10)
    assert rectangle.perimeter() == 30

def test_rectangle_set_dimensions():
    rectangle = Rectangle()
    rectangle.set_dimensions(7, 14)
    assert rectangle.get_dimensions() == (7, 14)

def test_circle_area():
    circle = Circle(7)
    assert circle.area() == pytest.approx(153.93804)

def test_circle_circumference():
    circle = Circle(7)
    assert circle.circumference() == pytest.approx(43.98226)