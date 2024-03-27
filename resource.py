class Resource:
    """Resource object"""

    def __init__(self, name, *, manufacturer=None, total=1):
        self.name = name
        self.manufacturer = manufacturer
        self._total = 0
        self._allocated = 0
        self._rest = None
        self.purchased(total)

    @property
    def total(self):
        return self._total

    @property
    def allocated(self):
        return self._allocated

    @property
    def category(self):
        return self.__class__.__name__.lower()

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

        self._allocated += n
        self._rest = None

    def free_up(self, n: int) -> None:
        """Return n resources to the pool."""

        if n > self.allocated:
            raise ValueError(
                f'Not enough resources!  {self.allocated} are allocated.'
            )

        self._allocated -= n
        self._rest = None

    def died(self, n: int) -> None:
        """Remove n resources from the pool."""

        if n >= self.total:
            raise ValueError('Not enough resources in the pool.')
        if n > self.rest:
            raise ValueError('Not enough free resources available.')

        self._total -= n
        self._rest = None

    def purchased(self, n: int) -> None:
        """Add inventory to the pool."""

        if self._total + n <= 0:
            raise ValueError('Total must be greater than 0!')

        self._total += n
        self._rest = None
