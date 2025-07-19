import pytest

from src.employee import (
    Employee,
    ExtendedEmployee
)

def test_employee_full_name():
    emp = Employee("Jane", "Doe")
    assert emp.get_full_name() == "Jane Doe"

def test_employee_address():
    emp = Employee("John", "Smith")
    emp.set_address("456 Elm St")
    assert emp.get_address() == "456 Elm St"

def test_employee_age():
    emp = Employee("Alice", "Johnson")
    emp.set_age(28)
    assert emp.get_age() == 28

def test_employee_department():
    emp = Employee("Bob", "Brown")
    emp.set_department("Marketing")
    assert emp.get_department() == "Marketing"

def test_extended_employee_salary():
    emp = ExtendedEmployee("Charlie", "Davis")
    emp.set_salary(60000)
    assert emp._get_salary() == 60000  