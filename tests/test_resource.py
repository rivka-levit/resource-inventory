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
