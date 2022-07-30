"""
This module provides an example of calculator testing.

Notes:
    1- Each class naming must be in form `*TestCase`
    2- Each method name must be in form `test_*`
        otherwise it wont be run.
    3- If a test fails it raises an `AssertionError`
"""

from unittest import TestCase
from calculator import add, sub, mul, div

class CalculatorTestCase(TestCase):
    """Test case class for `calculator`"""

    def setUp(self) -> None:
        self.a = 10
        self.b = 2

    def tearDown(self) -> None:
        del self.a
        del self.b


    # All tests

    def test_add(self):
        """Test `add` method"""

        # self.assertIsNotNone(add(self.a, self.b), "add must not return None")
        # self.assertEqual(add(self.a, self.b), 12)

        assert add(self.a, self.b) is not None #, "add must not return None"
        assert add(self.a, self.b) == 12

    def test_sub(self) -> None:
        """Test `sub` method"""

        assert sub(self.a, self.b) == 8

    def test_mul(self) -> None:
        """Test `mul` method"""

        assert mul(self.a, self.b) == 20

    def test_div(self) -> None:
        """Test `div` method"""

        assert div(self.a, self.b) == 5


    def general_method(self):
        """Not-a-test method"""

        print("This method is not a test")
