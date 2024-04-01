from app.resource import Resource


class CPU(Resource):
    """CPU resource"""

    def __init__(self, name, cores, socket, power_watts, *,
                 manufacturer=None, total=1):
        super().__init__(name, manufacturer=manufacturer, total=total)
        self._cores = cores
        self._socket = socket
        self._power_watts = power_watts

    @property
    def cores(self):
        return self._cores

    @property
    def socket(self):
        return self._socket

    @property
    def power_watts(self):
        return self._power_watts

    def __repr__(self):
        return (f'CPU(name={self.name}, cores={self.cores}, '
                f'socket={self.socket}, power_watts={self.power_watts})')
