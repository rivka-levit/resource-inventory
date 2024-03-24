class Resource:
    """Resource object"""

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Resource: {self.name}'

    def __repr__(self):
        return f'Resource(name={self.name})'
