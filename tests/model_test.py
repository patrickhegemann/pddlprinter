import pytest

from pddlprinter import PlanningProblem, NotDefinedException
from pddlprinter.parser import PDDLParser


@pytest.fixture
def chopper():
    s = """
    (define (domain chopper)
        ; -- snipped requirements --
        (:types
            tree apple - resource
            robot capacity
        )
        (:constants
            c0 c1 c2 c3 - capacity
        )
        (:predicates
            (on-tree ?a - apple ?t - tree)
            (in-robot ?res - resource ?r - robot)
            (collected ?res - resource)
            (has-capacity ?r - robot ?c - capacity)
            (next-capacity ?cap1 ?cap2 - capacity)
            (chopped ?t - tree)
        )
        ; -- snipped actions --
    )
    """
    return PDDLParser.parse_direct(s)


def test_infer_objects_simple(chopper):
    p = PlanningProblem(chopper, "apples")
    # Add 3 apples and check if they were added correctly
    for i in range(1, 4):
        p.init("on-tree", "apple%d" % i, "tree1")
        a = p.objects.get_object_by_name("apple%d" % i)
        assert a.name == "apple%d" % i
        assert a.object_type is chopper.get_type_from_name("apple")
    p.goal("chopped", "tree2")
    # Check if the 2 trees were added correctly
    for i in range(1, 3):
        t = p.objects.get_object_by_name("tree%d" % i)
        assert t.name == "tree%d" % i
        assert t.object_type is chopper.get_type_from_name("tree")
    # Initialize robot with a capacity
    p.init("has-capacity", "foo-bot", "c2")
    r = p.objects.get_object_by_name("foo-bot")
    # Check if robot has been added correctly
    assert r.name == "foo-bot"
    assert r.object_type is chopper.get_type_from_name("robot")
    # Shouldn't add constants again
    assert p.objects.get_object_by_name("c2") is None
    # So there should be 6 objects
    assert len(p.objects.objects) is 6
    # Add some predicates with only constants
    for i in range(1, 4):
        p.init("next-capacity", "c%d" % i, "c%d" % (i-1))
    # There should still be 6 objects
    assert len(p.objects.objects) is 6
    # 7 initial state atoms and 1 goal atom
    assert len(p.init_state.atoms) is 7
    assert len(p.goal_state.atoms) is 1


def test_add_object_manually(chopper):
    p = PlanningProblem(chopper, "foo")
    p.add_object("apple1", "apple")
    a = p.objects.get_object_by_name("apple1")
    assert a.name == "apple1"
    assert a.object_type == chopper.get_type_from_name("apple")


def test_add_object_bad_type(chopper):
    # Add object of a type that does not exist in the domain
    p = PlanningProblem(chopper, "foo")
    with pytest.raises(NotDefinedException):
        p.add_object("pear1", "pear")


def test_add_bad_atom(chopper):
    # Add atom to initial state with an invalid predicate
    p = PlanningProblem(chopper, "foo")
    with pytest.raises(NotDefinedException):
        p.init("nonexistent-predicate", "bar")
