"""Pytest with parameters"""
import pytest


DATA = [
    ('Tester1', 'QAMinds1'),
    ('Tester2', 'QAMinds2'),
    ('Tester3', 'QAMinds3'),
]


@pytest.mark.parametrize('first_name, last_name', DATA)
def test_one(first_name, last_name):
    """Test case demo 1."""
    print(f'{first_name}-{last_name}')

