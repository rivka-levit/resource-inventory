from app.utils.validators import validate_integer


class Resource:
    """Base class for resources."""

    def __init__(self, name, total, allocated, *, manufacturer=None):
        """

        Args:
            name (str): display name of the resource
            total (int): current total amount of resources
            allocated (int): current count of in-use resources
            manufacturer (str): resource manufacturer

        Note:
            `allocated` can not exceed `total`
        """

        self._name = name
        self._manufacturer = manufacturer

        validate_integer('total', total, min_value=0)
        self._total = total

        validate_integer(
            'allocated', allocated, 0, total,
            custom_max_message='Allocated inventory can not exceed the total '
                               'inventory!'
        )
        self._allocated = allocated

    @property
    def name(self):
        """
        Returns:
            str: the resource name
        """

        return self._name

    @property
    def manufacturer(self):
        """
        Returns:
            str: the resource manufacturer
        """

        return self._manufacturer

    @property
    def total(self):
        """
        Returns:
            int: the total inventory count
        """

        return self._total

    @property
    def allocated(self):
        """
        Returns:
            int: number of resources in-use
        """

        return self._allocated

    @property
    def category(self):
        """
        Returns:
            str: the resource category
        """

        return self.__class__.__name__.lower()

    @property
    def available(self):
        """
        Returns:
            int: number of resources available for use
        """

        return self.total - self.allocated

    def __str__(self):
        return self.name

    def __repr__(self):
        return (f'{self.name} ({self.category} - {self.manufacturer}): '
                f'total={self.total}, allocated={self.allocated}')

    def claim(self, num: int) -> None:
        """
        Claim num inventory items (if available)
        Args:
            num (int): number of inventory items to claim

        Returns:
            None
        """

        validate_integer(
            'num', num, 1, self.available,
            custom_max_message='Can not claim more than available!'
        )

        self._allocated += num

    def free_up(self, num: int) -> None:
        """
        Return an inventory item to the available pool.
        Args:
            num (int): number of items to return (can not exceed number in-use)

        Returns:
            None
        """

        validate_integer(
            'num', num, 1, self.allocated,
            custom_max_message='Can not return more than currently allocated!'
        )

        self._allocated -= num

    def died(self, num: int) -> None:
        """
        Deallocate and remove num of items from the inventory pool altogether.

        Args:
            num (int): number of items to remove from the inventory pool

        Returns:
            None
        """

        validate_integer(
            'num', num, 1, self.allocated,
            custom_max_message='Can not remove more than allocated!'
        )

        self._allocated -= num
        self._total -= num

    def purchased(self, num: int) -> None:
        """
        Add new inventory to the pool.

        Args:
            num (int): number of items to add to the pool

        Returns:
            None
        """

        validate_integer(
            'num', num, min_value=1,
            custom_min_message='Num must be greater than 0!'
        )

        self._total += num
