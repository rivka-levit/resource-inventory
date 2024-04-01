from unittest import TestCase
from app.storages import Storage, HDD, SSD


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

    def test_create_hdd_with_invalid_size_fails(self):
        """Test creating an HDD with invalid size raises an error."""

        with self.assertRaises(ValueError):
            HDD('Some HDD', 900, 35, 7200)

    def test_create_hdd_with_invalid_rpm_fails(self):
        """Test creating an HDD with invalid rpm raises an error."""

        with self.assertRaises(ValueError):
            HDD('Some HDD', 900, 3.5, 7200.35)


class TestSSD(TestCase):
    """Tests for SSD storage class."""

    def test_create_ssd_successfully(self):
        """Test creating an SSD successfully."""

        name = 'Some SSD'
        capacity = 1500
        interface = 'PCIe NVMe 3.0 x4'
        total = 25

        ssd = SSD(name, capacity, interface, total=total)

        self.assertEqual(ssd.name, name)
        self.assertEqual(ssd.capacity_gb, capacity)
        self.assertEqual(ssd.interface, interface)
        self.assertEqual(ssd.total, total)

    def test_create_ssd_with_int_interface(self):
        """Test creating a ssd with an integer interface."""

        ssd = SSD('Some SSD', 2000, 358)
        self.assertIsInstance(ssd.interface, str)
