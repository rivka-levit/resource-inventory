class Resource:
    """Resource object"""

    def __init__(self, name, manufacturer=None):
        self.name = name
        self.manufacturer = manufacturer

    def __str__(self):
        return f'Resource: {self.name}'

    def __repr__(self):
        return f'Resource(name={self.name})'
