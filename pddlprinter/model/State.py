# from pddlprinter import Atom


class State:
    """
    A state consisting of a set of atoms
    """
    def __init__(self):
        self.atoms = list()

    def add(self, atom):
        if atom not in self.atoms:
            self.atoms.append(atom)
        return self
