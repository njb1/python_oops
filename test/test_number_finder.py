import pytest

from src.number_finder import (
    ExtentedNumberFinder,
    NumberFinder
)

def test_find_max_number():
    finder = NumberFinder([10, 20, 30, 40, 51])
    assert finder.find_max_number() == 51

def test_find_min_number():
    finder = NumberFinder([10, 20, 30, 40, 51])
    assert finder.find_min_number() == 10

def test_find_average():
    finder = NumberFinder([10, 20, 30, 40, 51])
    assert finder.find_average() == 30

def test_find_total():
    finder = NumberFinder([10, 20, 30, 40, 51])
    assert finder.find_total() == 151

def test_is_in_list():
    finder = ExtentedNumberFinder([10, 20, 30, 40, 51])
    assert finder.is_in_list(30) is True
