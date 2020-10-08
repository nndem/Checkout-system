""""
Module represents class Entity description.
Can be expanded later.
"""


class Entity:
    """
    describes items basics
    """
    def __init__(self, entity_type):
        self._type = entity_type

    def __getattr__(self, attr):
        if attr == 'type':
            return self._type
