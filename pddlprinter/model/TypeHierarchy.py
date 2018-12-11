from pddlprinter.model import ObjectType


class TypeHierarchy:
    def __init__(self):
        self.types = []

    def update_type(self, name, children=[]):
        for t in self.types:
            if t.name == name:
                t.add_children(self.get_types_from_names(children))
                return t
        t = ObjectType(name, children)
        self.types.append(t)
        return t

    def get_type_from_name(self, name):
        for t in self.types:
            if t.name == name:
                return t
        return None

    def get_types_from_names(self, names=[]):
        name_types = []
        for n in names:
            for t in self.types:
                if t.name == n:
                    name_types.append(t)
        return name_types
