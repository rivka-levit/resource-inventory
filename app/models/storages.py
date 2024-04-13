from app.models.resource import Resource

from app.utils.validators import validate_integer


class Storage(Resource):
    """A base class for storage devices."""

    def __init__(self, name, total, allocated, capacity_gb, *,
                 manufacturer=None):
        """
        Args:
            name (str): display name of the resource
            total (int): current total amount of resources
            allocated (int): current count of in-use resources
            manufacturer (str): resource manufacturer
            capacity_gb (int): storage capacity in GB
        """

        super().__init__(name, total, allocated, manufacturer=manufacturer)
        validate_integer('capacity_gb', capacity_gb, min_value=1)
        self._capacity_gb = capacity_gb

    @property
    def capacity_gb(self):
        """
        Indicates the capacity (in GB) of the storage device.
        Returns: int
        """

        return self._capacity_gb

    def __repr__(self):
        return f'{self.category}: {self.capacity_gb} GB'


class HDD(Storage):
    """HDD type resources."""

    def __init__(self, name, total, allocated, capacity_gb, size, rpm, *,
                 manufacturer=None):
        """
        Args:
            name (str): display name of the resource
            total (int): current total amount of resources
            allocated (int): current count of in-use resources
            capacity_gb (int): storage capacity in GB
            size (str): indicates the device's size (must be either 2.5" or 3.5")
            rpm (int): disk rotation speed (in rpm)
            manufacturer (str): resource manufacturer
        """

        super().__init__(name, total, allocated, capacity_gb,
                         manufacturer=manufacturer)

        allowed_sizes = ('2.5"', '3.5"')
        if size not in allowed_sizes:
            raise ValueError(f'Invalid HDD size.'
                             f'Must be one of {', '.join(allowed_sizes)}')

        validate_integer('rpm', rpm, min_value=1000, max_value=50000)

        self._size = size
        self._rpm = rpm

    @property
    def size(self):
        """
        The HDD size (2.5" / 3.5")
        Returns: str
        """

        return self._size

    @property
    def rpm(self):
        """
        The HDD spin speed (rpm)
        Returns: int
        """

        return self._rpm

    def __repr__(self):
        s = super().__repr__()
        return f'{s} ({self.size}, {self.rpm} rpm)'


class SSD(Storage):
    """SSD type resources."""

    def __init__(self, name, total, allocated, capacity_gb, interface, *,
                 manufacturer=None):
        """
        Args:
            name (str): display name of the resource
            total (int): current total amount of resources
            allocated (int): current count of in-use resources
            capacity_gb (int): storage capacity in GB
            interface (str): indicates the device's interface (e.g. PCIe NVMe 3.0 x4)
            manufacturer (str): resource manufacturer
        """
        super().__init__(name, total, allocated, capacity_gb,
                         manufacturer=manufacturer)
        self._interface = interface

    @property
    def interface(self):
        """
        Interface used by SSD (e.g. PCIe NVMe 3.0 x4)
        Returns: str
        """

        return self._interface

    def __repr__(self):
        s = super().__repr__()
        return f'{s} ({self.interface})'
