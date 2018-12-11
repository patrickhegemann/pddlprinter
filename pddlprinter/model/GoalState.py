from pddlprinter.model.State import State


class GoalState(State):
    """
    Goal state for planning problems
    """
    def __str__(self):
        s = "\t(:goal (and\n"
        for atom in self.atoms:
            s += "\t\t%s\n" % str(atom)
        s += "\t))\n"
        return s
