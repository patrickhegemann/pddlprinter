class ObjectType:
    def __init__(self, name, children=[], parent=None):
        self.name = name
        self.children = []
        self.parent = None

        self.set_children(children)
        self.set_parent(parent)

    def set_children(self, children):
        self.children = children
        for c in children:
            c.set_parent(self)

    def set_parent(self, parent):
        self.parent = parent

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return str(self) == str(other)
