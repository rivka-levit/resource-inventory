from unittest import TestCase
from resource import Resource


class TestResourceInit(TestCase):
    def test_create_resource(self):
        """Test creating a resource instance with name."""

        resource = Resource('Intel Core i9-9900K')
        string_value = 'Resource: Intel Core i9-9900K'
        repr_value = 'Resource(name=Intel Core i9-9900K)'

        self.assertEqual(str(resource), string_value)
        self.assertEqual(repr(resource), repr_value)

    def test_create_resource_with_manufacturer(self):
        """Test creating a resource instance with manufacturer name."""

        mf = 'Nvidia'
        resource = Resource('GeForce Experience', manufacturer=mf)

        self.assertEqual(resource.manufacturer, mf)

    def test_create_resource_with_total_success(self):
        """Test creating a resource instance with total successfully."""

        total = 5
        resource = Resource('Intel Core i9-9900K', total=total)

        self.assertEqual(resource.total, total)

    def test_create_resource_with_neg_total_fails(self):
        """Test creating a resource instance with negative total fails."""

        total = -5
        with self.assertRaises(ValueError):
            Resource('Intel Core i9-9900K', total=total)

    def test_create_resource_with_zero_total_fails(self):
        """Test creating a resource instance with zero total fails."""

        total = 0
        with self.assertRaises(ValueError):
            Resource('Intel Core i9-9900K', total=total)
