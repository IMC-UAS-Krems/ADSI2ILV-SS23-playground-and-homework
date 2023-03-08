from triangle import is_valid_triangle
from triangle import type_of_triangle
from triangle import triangle
import pytest


def test_type_of_triangle():
    expected_type = 'Equilateral'
    actual_type = type_of_triangle(1, 1, 1)
    assert actual_type == expected_type


def test_triangle():
    expected_equilateral = 'Equilateral'
    actual7 = triangle(1, 1, 1)
    assert expected_equilateral == actual7


def test_exception():
    with pytest.raises(Exception):
        triangle('a', 'c', 'b')


def test_negative_int():
    with pytest.raises(Exception):
        triangle(-1, -1, -1)


def test_is_valid():
    expected_t = True
    actual2 = is_valid_triangle(1, 2, 3)
    assert expected_t == actual2


def test_0_false():
    expected_f = False
    actual1 = is_valid_triangle(0, 0, 0)
    assert expected_f == actual1


def test_string_false():
    expected_f = False
    actual3 = is_valid_triangle('a', 'a', 'aa')
    assert expected_f == actual3


def test_equilateral():
    expected_equilateral = 'Equilateral'
    actual4 = type_of_triangle(1, 1, 1)
    assert expected_equilateral == actual4


def test_isoceles():
    expected_isoceles = 'Isosceles'
    actual5 = type_of_triangle(1, 1, 2)
    assert expected_isoceles == actual5


def test_scalene():
    expected_scalene = 'Scalene'
    actual6 = type_of_triangle(1, 2, 3)
    assert expected_scalene == actual6
