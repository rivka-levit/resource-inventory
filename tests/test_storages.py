from unittest import TestCase
from storages import Storage


class TestStorage(TestCase):
    def test_create_storage_resource(self):
        storage = Storage('Some Storage', 120, total=5)

        self.assertEqual(storage.rest, 5)
        self.assertEqual(storage.capacity_gb, 120)

    def test_non_int_capacity_gb_error(self):
        """Test creating a storage with non-int capacity raises an error."""

        with self.assertRaises(ValueError):
            Storage('Some Storage', 120.53, total=5)
