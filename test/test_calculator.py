import pytest

from src.calculator import (
    Calculator,
    ExtendedCalculator
)

def test_calc_add():
    calc = Calculator(3, 2)
    assert calc.calc_add() == 5

def test_calc_minus():
    calc = Calculator(5, 3)
    assert calc.calc_minus() == 2

def test_calc_mult():
    calc = Calculator(4, 2)
    assert calc.calc_mult() == 8

def test_calc_div():
    calc = Calculator(8, 2)
    assert calc.calc_div() == 4

def test_calc_mod():
    calc = ExtendedCalculator(5, 2)
    assert calc.calc_mod() == 1

