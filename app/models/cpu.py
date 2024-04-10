from app.models.resource import Resource

from app.utils.validators import validate_integer


class CPU(Resource):
    """Resource subclass used to track specific CPU inventory pools."""

    def __init__(self, name, total, allocated, cores, socket, power_watts, *,
                 manufacturer=None):
        """
        Args:
            name (str): display name of the resource
            total (int): current total amount of resources
            allocated (int): current count of in-use resources
            cores (int): number of cores
            socket (str): CPU socket type
            power_watts (int): CPU rated wattage
            manufacturer (str): resource manufacturer
        """

        super().__init__(name, total, allocated, manufacturer=manufacturer)

        validate_integer('cores', cores, min_value=1)
        validate_integer('power_watts', power_watts, min_value=1)

        self._cores = cores
        self._socket = socket
        self._power_watts = power_watts

    @property
    def cores(self):
        """
        Number of cores.
        Returns: int
        """

        return self._cores

    @property
    def socket(self):
        """
        The socket type for CPU.
        Returns: str
        """

        return self._socket

    @property
    def power_watts(self):
        """
        The rated wattage for CPU.
        Returns: int
        """

        return self._power_watts

    def __repr__(self):
        return f'{self.category}: {self.name} ({self.socket} - x{self.cores})'
