from unittest import TestCase
from resource import Resource


class TestResourceInit(TestCase):
    def test_create_resource(self):
        """Test creating a resource instance with name."""

        resource = Resource('Intel Core i9-9900K')
        string_value = 'Intel Core i9-9900K'
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

    def test_create_resource_with_zero_allocated(self):
        """Test creating a resource instance with zero allocated."""

        resource = Resource('Intel Core i9', total=10)

        self.assertEqual(resource.allocated, 0)

    def test_create_resource_with_category_name(self):
        """Test creating a resource instance with category 'resource'."""

        resource = Resource('Intel Core i9', total=10)
        category = 'resource'

        self.assertEqual(resource.category, category)

    def test_rest_computed_property(self):
        """Test creating a resource instance with rest computed property."""

        resource = Resource('Intel Core i9', total=10)

        self.assertEqual(resource.rest, 10)


class TestResource(TestCase):
    """Test for Resource class functionality."""

    def setUp(self):
        self.resource = Resource('Intel Core i9-9900K',
                                 total=10,
                                 manufacturer='Intel')

    def test_claim_resource_success(self):
        """Test claim method of Resource class."""

        self.resource.claim(3)

        self.assertEqual(self.resource.allocated, 3)
        self.assertEqual(self.resource.rest, 7)

    def test_claim_unavailable_resource_fails(self):
        """Test claiming more resources than exist fails."""

        with self.assertRaises(ValueError):
            self.resource.claim(15)

    def test_claim_not_rest_resource_fails(self):
        """Test claiming more resources than rest fails."""

        self.resource.claim(5)

        with self.assertRaises(ValueError):
            self.resource.claim(8)

    def test_free_up_resource_success(self):
        """Test free up method of Resource class."""

        self.resource.claim(4)
        self.resource.free_up(2)

        self.assertEqual(self.resource.allocated, 2)
        self.assertEqual(self.resource.rest, 8)

    def test_free_up_not_allocated_resource_fails(self):
        """Test free up more resources than allocated fails."""

        self.resource.claim(5)

        with self.assertRaises(ValueError):
            self.resource.free_up(7)

    def test_remove_resource_success(self):
        """Test died method of Resource class."""

        self.resource.died(1)

        self.assertEqual(self.resource.total, 9)
        self.assertEqual(self.resource.rest, 9)

    def test_remove_resource_not_available_fails(self):
        """Test removing a resource that is not available fails."""

        self.resource.claim(9)

        with self.assertRaises(ValueError):
            self.resource.died(2)
