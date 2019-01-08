from pddlprinter.model import Predicate


class Atom:
    """
    An atom/statement consisting of predicate name and its specific arguments
    """
    def __init__(self, predicate, objects, negated=False):
        self.predicate = predicate
        self.objects = objects
        self.negated = negated

        if type(predicate) is Predicate:
            if not predicate.check_types(objects):
                print("WARNING: object types don't match")

    def __str__(self):
        if self.negated:
            if len(self.objects) is 0:
                return "(not (%s))" % self.predicate
            else:
                return "(not (%s %s))" % (self.predicate, " ".join([str(obj) for obj in self.objects]))
        else:
            if len(self.objects) is 0:
                return "(%s)" % self.predicate
            else:
                return "(%s %s)" % (self.predicate, " ".join([str(obj) for obj in self.objects]))

    def __eq__(self, other):
        return str(self) == str(other)
