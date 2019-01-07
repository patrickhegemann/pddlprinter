import pytest
from pddlprinter.parser import *


@pytest.fixture
def foo_domain():
    domain_text = """
        (define (domain foo)
            ;comment
            (:types
                ; comment
                mega-bot - robot    ; another comment
                robot
                location
            )
            (:predicates
                (at ?r - robot ?l - location)
                (has-fuel ?m - mega-bot)   
                (finalized)
                ; yet another comment
            )
            (:constants
                foo bar - robot
                baz - mega-bot l1 l2 l3 - location
            )
        )
        """
    return PDDLParser.parse_direct(domain_text)


def test_parser_name(foo_domain):
    assert foo_domain.name == "foo"


def test_parser_types(foo_domain):
    assert len(foo_domain.type_hierarchy.types) == 3
    robot_type = foo_domain.get_type_from_name("robot")
    megabot_type = foo_domain.get_type_from_name("mega-bot")
    assert robot_type.name == "robot"
    assert robot_type.parent is None
    assert megabot_type.name == "mega-bot"
    assert megabot_type.parent is robot_type
    location_type = foo_domain.get_type_from_name("location")
    assert location_type.name == "location"
    assert location_type.parent is None


def test_parser_predicates(foo_domain):
    assert len(foo_domain.predicates) == 3
    robot_type = foo_domain.get_type_from_name("robot")
    location_type = foo_domain.get_type_from_name("location")
    at_predicate = foo_domain.get_predicate_by_name("at")
    assert at_predicate.name == "at"
    assert len(at_predicate.types) is 2
    assert at_predicate.types[0] is robot_type
    assert at_predicate.types[1] is location_type
    has_fuel_predicate = foo_domain.get_predicate_by_name("has-fuel")
    assert has_fuel_predicate.name == "has-fuel"
    assert len(has_fuel_predicate.types) is 1
    assert has_fuel_predicate.types[0] is foo_domain.get_type_from_name("mega-bot")
    finalized_predicate = foo_domain.get_predicate_by_name("finalized")
    assert finalized_predicate.name == "finalized"
    assert len(finalized_predicate.types) is 0


def test_parser_constants(foo_domain):
    assert len(foo_domain.constants) == 6
    foo_bot = foo_domain.get_constant_by_name("foo")
    assert foo_bot.name == "foo"
    assert foo_bot.object_type is foo_domain.get_type_from_name("robot")
    baz_bot = foo_domain.get_constant_by_name("baz")
    assert baz_bot.name == "baz"
    assert baz_bot.object_type is foo_domain.get_type_from_name("mega-bot")
    for i in range(1, 4):
        loc = foo_domain.get_constant_by_name("l%d" % i)
        assert loc.name == "l%d" % i
        assert loc.object_type is foo_domain.get_type_from_name("location")
