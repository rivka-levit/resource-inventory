"""
Tests for CPU class.
Command line: python -m unittest -v tests.test_cpu
"""

from unittest import TestCase
from app.models.cpu import CPU


class TestCPU(TestCase):
    """Tests for CPU class."""

    def setUp(self):
        self.cpu_values = {
            'name': 'RYZEN Threadripper 2990WX',
            'total': 10,
            'allocated': 3,
            'cores': 32,
            'socket': 'sTR4',
            'power_watts': 250,
            'manufacturer': 'AMD',
        }

    def test_create_cpu_resource(self):
        """Test creating CPU resource."""

        cpu = CPU(**self.cpu_values)

        for key, value in self.cpu_values.items():
            self.assertEqual(getattr(cpu, key), value)

    def test_cpu_representation(self):
        """Test CPU representation."""

        expected_repr = (f'cpu: {self.cpu_values["name"]} '
                         f'({self.cpu_values["socket"]} - '
                         f'x{self.cpu_values["cores"]})')

        cpu = CPU(**self.cpu_values)

        self.assertEqual(repr(cpu), expected_repr)
