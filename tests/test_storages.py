"""
Tests for Storages.
Command line: python -m unittest -v tests.test_storages
"""

from unittest import TestCase
from app.models.storages import Storage, HDD, SSD


class TestStorage(TestCase):

    def setUp(self):
        self.values = {
            'name': 'Thumbdrive',
            'total': 10,
            'allocated': 3,
            'capacity_gb': 512,
            'manufacturer': 'Sundisk'
        }

    def test_create_storage_resource(self):
        """Test creating a storage resource successfully."""

        storage = Storage(**self.values)

        for key, value in self.values.items():
            self.assertEqual(getattr(storage, key), value)

    def test_invalid_capacity_gb_error(self):
        """Test creating a storage with invalid capacity raises an error."""

        test_values = [(10.5, TypeError), (-1, ValueError), (0, ValueError)]
        for capacity, exception in test_values:
            with self.assertRaises(exception):
                self.values['capacity_gb'] = capacity
                Storage(**self.values)

    def test_storage_repr(self):
        """Test storage representation."""

        storage = Storage(**self.values)

        self.assertIn('storage', repr(storage))
        self.assertIn('512 GB', repr(storage))


class TestHDD(TestCase):
    """Tests for HDD storage class."""

    def setUp(self):
        self.values = {
            'name': '1TB SATA HDD',
            'total': 10,
            'allocated': 3,
            'capacity_gb': 1000,
            'size': '3.5"',
            'rpm': 10000,
            'manufacturer': 'Seagate'
        }

    def test_create_hdd_storage(self):
        """Test creating hdd storage successfully."""

        repr_expected = (f'hdd: {self.values["capacity_gb"]} GB '
                         f'({self.values["size"]}, {self.values["rpm"]} rpm)')

        hdd = HDD(**self.values)

        for key, value in self.values.items():
            self.assertEqual(getattr(hdd, key), value)

        self.assertEqual(repr(hdd), repr_expected)

    def test_create_hdd_with_invalid_size_fails(self):
        """Test creating an HDD with invalid size raises an error."""

        self.values['size'] = '2.8"'

        with self.assertRaises(ValueError):
            HDD(**self.values)

    def test_create_hdd_with_invalid_rpm_fails(self):
        """Test creating an HDD with invalid rpm raises an error."""

        test_values = [
            (1000.5, TypeError),
            (5, ValueError),
            (50500, ValueError)
        ]

        for value, exception in test_values:
            self.values['rpm'] = value

            with self.assertRaises(exception):
                HDD(**self.values)


class TestSSD(TestCase):
    """Tests for SSD storage class."""

    def setUp(self):
        self.values = {
            'name': 'Samsung 860 EVO',
            'total': 10,
            'allocated': 3,
            'capacity_gb': 1000,
            'interface': 'SATA III',
            'manufacturer': 'Samsung'
        }

    def test_create_ssd_successfully(self):
        """Test creating an SSD successfully."""

        ssd = SSD(**self.values)

        for key, value in self.values.items():
            self.assertEqual(getattr(ssd, key), value)

    def test_repr_ssd(self):
        """Test ssd representation."""

        ssd = SSD(**self.values)

        self.assertIn(ssd.category, repr(ssd))
        self.assertIn(str(self.values['capacity_gb']), repr(ssd))
        self.assertIn(self.values['interface'], repr(ssd))
