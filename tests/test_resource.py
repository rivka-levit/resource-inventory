"""
Tests the Resource class.
Command line: python -m unittest -v tests.test_resource
"""

from unittest import TestCase
from app.models.resource import Resource


class TestResourceInit(TestCase):
    def test_create_resource(self):
        """Test creating a resource instance successfully."""

        name = 'Intel Core i9-9900K'
        total = 10
        allocated = 5
        mf = 'Nvidia'
        category = 'resource'

        string_expected = 'Intel Core i9-9900K'
        repr_expected = (f'{name} ({category} - {mf}): '
                         f'total={total}, allocated={allocated}')
        available_expected = total - allocated

        resource = Resource(name, total, allocated, manufacturer=mf)

        self.assertEqual(resource.name, name)
        self.assertEqual(resource.category, category)
        self.assertEqual(resource.total, total)
        self.assertEqual(resource.allocated, allocated)
        self.assertEqual(resource.manufacturer, mf)
        self.assertEqual(resource.available, available_expected)
        self.assertEqual(str(resource), string_expected)
        self.assertEqual(repr(resource), repr_expected)


class TestResource(TestCase):
    """Test for Resource class functionality."""

    def setUp(self):
        self.resource = Resource('Intel Core i9-9900K', 10, 5,
                                 manufacturer='Intel')

    def test_claim_resource_success(self):
        """Test claim method of Resource class."""

        self.resource.claim(3)

        self.assertEqual(self.resource.allocated, 8)
        self.assertEqual(self.resource.available, 2)

    def test_claim_unavailable_resource_fails(self):
        """Test claiming more resources than exist fails."""

        with self.assertRaises(ValueError):
            self.resource.claim(15)

    def test_claim_not_available_resource_fails(self):
        """Test claiming more resources than available fails."""

        self.resource.claim(5)

        with self.assertRaises(ValueError):
            self.resource.claim(8)

    def test_free_up_resource_success(self):
        """Test free up method of Resource class."""

        self.resource.free_up(2)

        self.assertEqual(self.resource.allocated, 3)
        self.assertEqual(self.resource.available, 7)

    def test_free_up_not_allocated_resource_fails(self):
        """Test free up more resources than allocated fails."""

        with self.assertRaises(ValueError):
            self.resource.free_up(7)

    def test_remove_resource_success(self):
        """Test died method of Resource class."""

        self.resource.died(1)

        self.assertEqual(self.resource.total, 9)
        self.assertEqual(self.resource.allocated, 4)

    def test_remove_resource_not_allocated_fails(self):
        """Test removing more resources than allocated fails."""

        with self.assertRaises(ValueError):
            self.resource.died(8)

    def test_purchase_resource_success(self):
        """Test purchased method of Resource class."""

        self.resource.purchased(5)
        self.assertEqual(self.resource.total, 15)
        self.assertEqual(self.resource.available, 10)
