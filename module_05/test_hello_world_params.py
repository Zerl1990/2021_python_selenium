"""Pytest with parameters"""
import pytest


DATA = [
    ('Tester1', 'pass1'),
    ('Tester2', 'pass2'),
    ('Tester3', 'pass3'),
]


@pytest.mark.parametrize('user, password', DATA)
def test_one(user, password):
    """Test case demo 1."""
    print(f'{user}-{password}')
