from unittest import TestCase
from cpu import CPU


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
