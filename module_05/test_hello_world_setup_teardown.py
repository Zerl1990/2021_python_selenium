"""Pytest with parameters"""
import pytest


class TestClass:
    """Test class."""

    @classmethod
    def setup_class(cls):
        print('Class setup')

    @classmethod
    def teardown_class(cls):
        print('Class teardown')

    def setup_method(self):
        """Setup method"""
        print('Method setup')

    def teardown_method(self):
        """Teardown method"""
        print('Method teardown')

    def test_one(self):
        print(f'Hello world 1')

    def test_two(self):
        print(f'Hello world 2')

    def test_three(self):
        print(f'Hello world 3')
