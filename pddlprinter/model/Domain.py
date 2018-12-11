class Domain:
    def __init__(self):
        self.name = ""
        self.type_hierarchy = None
        self.predicates = []
        self.constants = []

    def get_type_from_name(self, name):
        return self.type_hierarchy.get_type_from_name(name)

    def get_predicate_by_name(self, name):
        for p in self.predicates:
            if p.name == name:
                return p
        return None

    def get_constant_by_name(self, name):
        for c in self.constants:
            if c.name == name:
                return c
        return None
