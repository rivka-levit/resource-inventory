"""
Tests the validator functions.
Command line: python -m unittest -v tests.test_validators
"""

from unittest import TestCase

from app.utils.validators import validate_integer


class TestIntegerValidator(TestCase):
    """Test validate_integer function."""

    def test_valid(self):
        """Test validating an integer successfully."""

        validate_integer('arg', 10, 0, 20, 'custom min msg', 'custom max msg')

    def test_type_error(self):
        """
        Test validation raises an error when the argument is not an integer.
        """

        with self.assertRaises(TypeError):
            validate_integer('arg', 1.5, 0, 20)

    def test_min_std_err_msg(self):
        """
        Test validation raises an error when the argument is less than
        minimum value.
        """

        with self.assertRaises(ValueError) as e:
            validate_integer('arg', -5, 0, 20)

        self.assertIn('arg', e.exception.args[0])
        self.assertIn('0', e.exception.args[0])

    def test_min_custom_err_msg(self):
        """
        Test validation raises an error when the argument is less than
        minimum value, and gives a custom error message.
        """

        with self.assertRaises(ValueError) as e:
            validate_integer('arg', -5, 0, 20, 'custom min msg')

        self.assertEqual('custom min msg', e.exception.args[0])

    def test_max_std_err_msg(self):
        """
        Test validation raises an error when the argument is greater than
        maximum value.
        """

        with self.assertRaises(ValueError) as e:
            validate_integer('arg', 25, 0, 20)

        self.assertIn('arg', e.exception.args[0])
        self.assertIn('20', e.exception.args[0])

    def test_max_custom_err_msg(self):
        """
        Test validation raises an error when the argument is greater than
        maximum value, and gives a custom error message.
        """

        with self.assertRaises(ValueError) as e:
            validate_integer('arg', 25, 0, 20,
                             'custom min msg', 'custom max msg')

        self.assertEqual('custom max msg', e.exception.args[0])
