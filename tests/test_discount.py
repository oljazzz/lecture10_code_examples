import pytest

from unittest_examples.discount import calculate_discount


def test_discount_basic():
    assert calculate_discount(100, 10) == 90


def test_discount_negative_percentage():
    with pytest.raises(ValueError):
        calculate_discount(100, -5)


def test_discount_over_100():
    with pytest.raises(ValueError):
        calculate_discount(100, 150)
