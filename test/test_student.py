import pytest

from src.student import (
    Student,
    StudentCalculator
)

def test_student_initialization():
    student = Student("John", "Doe")
    assert student.first_name == "John"
    assert student.last_name == "Doe"
    assert student.get_name() == "John Doe"

def test_set_name():
    student = Student("John", "Doe")
    student.set_name("Jane", "Smith")
    assert student.first_name == "Jane"
    assert student.last_name == "Smith"
    assert student.get_name() == "Jane Smith"

def test_set_address():
    student = Student("John", "Doe")
    student.set_address("123 Main St")
    assert student.get_address() == "123 Main St"

def test_set_age():
    student = Student("John", "Doe")
    student.set_age(20)
    assert student.get_age() == 20

def test_student_calculator_initialization():
    student_calc = StudentCalculator("John", "Doe", [85, 90, 78])
    assert student_calc.first_name == "John"
    assert student_calc.last_name == "Doe"
    assert student_calc.marks == [85, 90, 78]

def test_calculate_average():
    student_calc = StudentCalculator("John", "Doe", [85, 90, 78])
    average = student_calc.calculate_average()
    assert average == pytest.approx(84)