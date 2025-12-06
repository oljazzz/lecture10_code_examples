import pytest

from unittest_examples.math_utils import add, divide


def test_add_basic():
    assert add(2, 3) == 5


def test_divide_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
#
#
# def test_divide_negative():
#     with pytest.raises(ValueError):
#         divide(-2, 0)
#
#
# def test_is_even():
#     assert is_even(add(100, 89)) == False


