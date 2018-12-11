from pddlprinter.model import PDDLObject


class Predicate:
    def __init__(self, name, types):
        self.name = name
        self.types = types

    def check_types(self, objects):
        print("check")
        for (o, t) in zip(objects, self.types):
            print(o, t)
            if type(o) is not PDDLObject:
                continue
            if o.object_type is not t:
                return False
        return True

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return str(self) == str(other)
