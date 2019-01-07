from pddlprinter import NotDefinedException
from pddlprinter.model import InitialState, GoalState, ObjectSet, PDDLObject, Atom


class PlanningProblem:
    """
    Generic planning problem class
    """
    def __init__(self, domain, problem_name):
        self.domain = domain
        self.problem_name = problem_name
        self.objects = ObjectSet()
        self.init_state = InitialState()
        self.goal_state = GoalState()

        # todo: make this clean ...
        self._metric = ""
        self.fluents = []

    def add_object(self, name, obj_type):
        t = self.domain.type_hierarchy.get_type_from_name(obj_type)
        if t is None:
            raise NotDefinedException("Type %s is not defined in domain" % obj_type)
        o = PDDLObject(name, t)
        self.objects.add(o)
        return o

    def add_atom_to_state(self, predicate, object_names, state, negated=False):
        p = self.domain.get_predicate_by_name(predicate)
        if p is None:
            raise NotDefinedException("Predicate %s not defined in domain" % predicate)

        counter = 0
        pddl_objects = []
        for n in object_names:
            # Object is a constant -> Don't add new object
            new_obj = self.domain.get_constant_by_name(n)
            if new_obj is not None:
                pddl_objects.append(new_obj)
                counter += 1
                continue
            # Object has already been added -> Don't add new object
            new_obj = self.objects.get_object_by_name(n)
            if new_obj is not None:
                pddl_objects.append(new_obj)
                counter += 1
                continue

            # Create new object
            o = self.add_object(n, p.types[counter])
            pddl_objects.append(o)
            counter += 1

        state.add(Atom(p, pddl_objects, negated))
        return state

    def init(self, predicate, *object_names, negated=False):
        self.init_state = self.add_atom_to_state(predicate, list(object_names), self.init_state, negated)

    # todo: make this good
    def init_fluent(self, fluent, value):
        self.init_state.fluents.append((fluent, value))

    def goal(self, predicate, *object_names, negated=False):
        self.goal_state = self.add_atom_to_state(predicate, list(object_names), self.goal_state, negated)

    # todo: make this good
    def metric(self, opt_type, function):
        self._metric = "\t(:metric %s (%s))\n" % (opt_type, function)
        
    def __str__(self):
        s = "(define (problem %s)\n" % self.problem_name
        s += "\t(:domain %s)\n" % self.domain.name
        s += str(self.objects)
        s += str(self.init_state)
        s += str(self.goal_state)
        s += str(self._metric)      # todo
        s += ")\n"
        return s 
