class Resource:
    """Resource object"""

    def __init__(self, name, manufacturer=None, total=1):
        self.name = name
        self.manufacturer = manufacturer
        self.total = total

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        if value <= 0:
            raise ValueError('Total must be greater than 0!')
        self._total = value

    def __str__(self):
        return f'Resource: {self.name}'

    def __repr__(self):
        return f'Resource(name={self.name})'
