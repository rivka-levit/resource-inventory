"""
Tests for Resource class.
Command line: python -m unittest -v tests.test_resource
"""

from unittest import TestCase
from app.models.resource import Resource


class TestResourceInit(TestCase):
    """Test __init__ method of Resource class."""

    def setUp(self):
        self.values = {
            'name': 'Intel Core i9-9900K',
            'total': 10,
            'allocated': 5,
            'manufacturer': 'Intel'
        }

    def test_create_resource(self):
        """Test creating a resource instance successfully."""

        category = 'resource'
        available_expected = self.values['total'] - self.values['allocated']

        resource = Resource(**self.values)

        for key, value in self.values.items():
            self.assertEqual(getattr(resource, key), value)

        self.assertEqual(resource.category, category)
        self.assertEqual(resource.available, available_expected)


class TestResource(TestCase):
    """Test for Resource class functionality."""

    def setUp(self):
        self.values = {
            'name': 'Intel Core i9-9900K',
            'total': 10,
            'allocated': 5,
            'manufacturer': 'Intel'
        }
        self.resource = Resource(**self.values)

    def test_str_method(self):
        """Test string representation of Resource."""

        self.assertEqual(str(self.resource), self.values['name'])

    def test_repr_method(self):
        """Test __repr__ of Resource class."""

        category = type(self.resource).__name__.lower()
        repr_expected = (f'{self.values['name']} ({category} - '
                         f'{self.values['manufacturer']}): '
                         f'total={self.values['total']}, '
                         f'allocated={self.values['allocated']}')

        self.assertEqual(repr(self.resource), repr_expected)

    def test_claim_resource_success(self):
        """Test claim method of Resource class."""

        claim_val = 3

        self.resource.claim(claim_val)

        allocated_expected = self.values['allocated'] + claim_val
        available_expected = self.values['total'] - allocated_expected

        self.assertEqual(self.resource.allocated, allocated_expected)
        self.assertEqual(self.resource.available, available_expected)

    def test_claim_resource_not_exist_fails(self):
        """Test claiming more resources than exist fails."""

        claim_val = self.values['total'] + 5

        with self.assertRaises(ValueError):
            self.resource.claim(claim_val)

    def test_claim_not_available_resource_fails(self):
        """Test claiming more resources than available fails."""

        claim_val = self.resource.available + 5

        with self.assertRaises(ValueError):
            self.resource.claim(claim_val)

    def test_claim_invalid_number_resources_fails(self):
        """Test claiming negative or zero number of resources fails."""

        values = [-1, 0]

        for n in values:
            with self.assertRaises(ValueError):
                self.resource.claim(n)

    def test_free_up_resource_success(self):
        """Test free up method of Resource class."""

        free_val = 1
        allocated_expected = self.values['allocated'] - free_val
        available_expected = self.values['total'] - allocated_expected

        self.resource.free_up(free_val)

        self.assertEqual(self.resource.allocated, allocated_expected)
        self.assertEqual(self.resource.available, available_expected)

    def test_free_up_not_allocated_resource_fails(self):
        """Test free up more resources than allocated fails."""

        free_val = self.values['allocated'] + 1

        with self.assertRaises(ValueError):
            self.resource.free_up(free_val)

    def test_free_up_invalid_number_resources_fails(self):
        """Test free up negative or zero number of resources fails."""

        values = [-1, 0]

        for n in values:
            with self.assertRaises(ValueError):
                self.resource.free_up(n)

    def test_remove_resource_success(self):
        """Test died method of Resource class."""

        died_val = 1
        total_expected = self.values['total'] - died_val
        allocated_expected = self.values['allocated'] - died_val

        self.resource.died(died_val)

        self.assertEqual(self.resource.total, total_expected)
        self.assertEqual(self.resource.allocated, allocated_expected)

    def test_remove_resource_not_allocated_fails(self):
        """Test removing more resources than allocated fails."""

        died_val = self.values['allocated'] + 1

        with self.assertRaises(ValueError):
            self.resource.died(died_val)

    def test_died_invalid_number_resources_fails(self):
        """Test removing negative or zero number of resources fails."""

        values = [-1, 0]

        for n in values:
            with self.assertRaises(ValueError):
                self.resource.died(n)

    def test_purchase_resource_success(self):
        """Test purchased method of Resource class."""

        purchase_val = 5
        total_expected = self.values['total'] + purchase_val
        available_expected = total_expected - self.resource.allocated

        self.resource.purchased(purchase_val)
        self.assertEqual(self.resource.total, total_expected)
        self.assertEqual(self.resource.available, available_expected)

    def test_purchase_invalid_number_resources_fails(self):
        """Test purchase negative or zero number of resources fails."""

        values = [-1, 0]

        for n in values:
            with self.assertRaises(ValueError):
                self.resource.purchased(n)
