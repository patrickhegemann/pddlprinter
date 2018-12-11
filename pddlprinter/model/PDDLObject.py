
class PDDLObject:
    """
    An object in a planning problem
    """
    def __init__(self, name, object_type=None, type_flexible=True):
        """
        Constructor
        :param name: Name of the object
        :param object_type: Type of the object
        :param type_flexible: Whether type of this object may be specialized in order to fit predicates
        """
        self.name = name
        self.object_type = object_type
        self.type_flexible = type_flexible

    def __str__(self):
        return self.name

    # def __eq__(self, other):
    #    return str(self) == str(other)

    def __hash__(self):
        return hash(self.name)
