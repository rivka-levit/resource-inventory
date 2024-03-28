from unittest import TestCase
from storages import Storage, HDD


class TestStorage(TestCase):
    def test_create_storage_resource(self):
        storage = Storage('Some Storage', 120, total=5)

        self.assertEqual(storage.rest, 5)
        self.assertEqual(storage.capacity_gb, 120)

    def test_non_int_capacity_gb_error(self):
        """Test creating a storage with non-int capacity raises an error."""

        with self.assertRaises(ValueError):
            Storage('Some Storage', 120.53, total=5)


class TestHDD(TestCase):
    """Tests for HDD storage class."""

    def test_create_hdd_storage(self):
        """Test creating hdd storage successfully."""

        name = 'Some HDD'
        capacity = 900
        size = 3.5
        rpm = 7200
        str_expected = f'HDD {name}, {capacity} GB, {size}"'
        repr_expected = f'HDD(name={name}, capacity={capacity}, size={size})'
        hdd = HDD(name, capacity, size, rpm, total=15)

        self.assertEqual(hdd.size, size)
        self.assertEqual(hdd.rpm, rpm)
        self.assertEqual(hdd.capacity_gb, capacity)
        self.assertEqual(str(hdd), str_expected)
        self.assertEqual(repr(hdd), repr_expected)
