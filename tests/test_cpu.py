from unittest import TestCase
from app.cpu import CPU


class TestCPU(TestCase):
    """Tests for CPU class."""

    def test_create_cpu_resource(self):

        name = '5 x AMD Ryzen'
        cores = 2
        socket = 'AM4'
        power = '94'

        cpu = CPU(name=name, cores=cores, socket=socket, power_watts=power)

        self.assertEqual(cpu.cores, cores)
        self.assertEqual(cpu.socket, socket)
        self.assertEqual(cpu.power_watts, power)

    def test_cpu_representation(self):
        """Test CPU representation."""

        name = '5 x AMD Ryzen'
        cores = 2
        socket = 'AM4'
        power = '94'
        expected_repr = (f'CPU(name={name}, cores={cores}, socket={socket}, '
                         f'power_watts={power})')

        cpu = CPU(name=name, cores=cores, socket=socket, power_watts=power)

        self.assertEqual(repr(cpu), expected_repr)
