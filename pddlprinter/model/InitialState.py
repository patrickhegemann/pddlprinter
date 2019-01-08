from pddlprinter.model.State import State


class InitialState(State):
    """
    Initial state for planning problems
    """
    def __init__(self):
        super().__init__()
        self.fluents = []   # todo

    def __str__(self):
        s = "\t(:init\n"
        for atom in self.atoms:
            s += "\t\t%s\n" % str(atom)
        for f in self.fluents:
            s += "\t\t(= (%s) %d)\n" % f
        s += "\t)\n"
        return s
