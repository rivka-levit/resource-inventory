class Resource:
    """Resource object"""

    def __init__(self, name, manufacturer=None, total=1):
        self.name = name
        self.manufacturer = manufacturer
        self.total = total
        self._allocated = 0
        self._category = None
        self._rest = None

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        if value <= 0:
            raise ValueError('Total must be greater than 0!')
        self._total = value
        self._rest = None

    @property
    def allocated(self):
        return self._allocated

    @allocated.setter
    def allocated(self, value):
        if value > self.total:
            raise ValueError('There are no enough resources available.')
        self._allocated = value
        self._rest = None

    @property
    def category(self):
        if self._category is None:
            self._category = self.__class__.__name__.lower()
        return self._category

    @property
    def rest(self):
        if self._rest is None:
            self._rest = self.total - self.allocated
        return self._rest

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'Resource(name={self.name})'

    def claim(self, n: int) -> None:
        """Take resources from the pool (as long as inventory is available)."""

        if n > self.total or n > self.rest:
            raise ValueError(
                f'Not enough resources! {self.rest} is available.'
            )

        self.allocated += n
