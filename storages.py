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
