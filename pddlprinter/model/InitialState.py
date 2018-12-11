from pddlprinter.model.State import State


class InitialState(State):
    """
    Initial state for planning problems
    """
    def __str__(self):
        s = "\t(:init\n"
        for atom in self.atoms:
            s += "\t\t%s\n" % str(atom)
        s += "\t)\n"
        return s
