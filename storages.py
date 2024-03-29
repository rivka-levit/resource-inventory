from resource import Resource


class Storage(Resource):
    def __init__(self, name, capacity_gb, *, manufacturer=None, total=1):
        super().__init__(name, manufacturer=manufacturer, total=total)
        self.capacity_gb = capacity_gb

    @property
    def capacity_gb(self):
        return self._capacity_gb

    @capacity_gb.setter
    def capacity_gb(self, value):
        if not isinstance(value, int):
            raise ValueError('Capacity_gb must be an integer!')
        self._capacity_gb = value


class HDD(Storage):
    """HDD resources."""

    def __init__(self, name, capacity_gb, size, rpm, *, manufacturer=None,
                 total=1):

        super().__init__(name, capacity_gb, manufacturer=manufacturer,
                         total=total)
        self.size = size
        self.rpm = rpm

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        allowed_sizes = (2.5, 3.5)
        if value not in allowed_sizes:
            raise ValueError('HDD size must be 2.5" or 3.5"')
        self._size = value

    @property
    def rpm(self):
        return self._rpm

    @rpm.setter
    def rpm(self, value):
        if not isinstance(value, int):
            raise ValueError('RPM must be an integer!')
        self._rpm = value

    def __str__(self):
        return f'HDD {self.name}, {self.capacity_gb} GB, {self.size}"'

    def __repr__(self):
        return (f'HDD(name={self.name}, '
                f'capacity={self.capacity_gb}, '
                f'size={self.size})')


class SSD(Storage):
    """SSD storages."""

    def __init__(self, name, capacity_gb, interface, *, manufacturer=None,
                 total=1):
        super().__init__(name, capacity_gb, manufacturer=manufacturer,
                         total=total)
        self.interface = interface

    @property
    def interface(self):
        return self._interface

    @interface.setter
    def interface(self, value):
        if not isinstance(value, str):
            try:
                value = str(value)
            except TypeError:
                raise ValueError('Interface must be a string!')

        self._interface = value

    def __str__(self):
        return f'SSD {self.name} {self.capacity_gb} GB, {self.interface}'

    def __repr__(self):
        return (f'SSD(name={self.name}, '
                f'capacity={self.capacity_gb}, '
                f'interface={self.interface})')
