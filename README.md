# PDDLPrinter

This is a Python3 module aimed at convenient generation of problems in PDDL for Automated Planning and is currently in early development. It helps you by doing the grunt work such as declaring objects and generating valid PDDL, so you can focus on creating good problem instances.

## Features

* Parsing domain file to infer types, constants and predicates for use in problem generation
* Initialization of predicates
* Conjunctive goals
* Automatic declaration of necessary objects, including simple type inference

Experimental Features:
* Specification of a metric (only a single function, not an arbitrary expression)
* Initialization of numeric fluents

Planned Features:
* Arbitrary goals
* Derived predicates
* Specification of arbitrary metrics, preferences
* Complete (automatic) type inference for objects
* Full support of PDDL 3.1 features
* Generation helpers (for grids, number sequences, graphs, ...)


## Installation (pip)

This module is not on the [Python Package Index](https://pypi.org) (yet), so you can clone this repository and [install it from source](https://packaging.python.org/tutorials/installing-packages/#installing-from-a-local-src-tree):
```
$ pip install /path/to/pddlprinter
```

## Example

Here is an example script that generates a classic Gripper problem with 6 balls:

```python
from pddlprinter.model import PlanningProblem
from pddlprinter.parser import PDDLParser

# Parse the Gripper domain file
dom = PDDLParser.parse("gripper.pddl")

# Create our new planning problem and give it a name
problem = PlanningProblem(dom, "gripper-example")

# Initialize the robot in room a ("at-robby" predicate with parameter "rooma")
problem.init("at-robby", "rooma")
# Initialize two grippers
problem.init("free", "gripper-left")
problem.init("free", "gripper-right")
# 6 balls start in room a and must get to room b
for i in range(1, 7):
    problem.init("at", "ball%d" % i, "rooma")
    problem.goal("at", "ball%d" % i, "roomb")

# Done!
print(problem)

```

Output:
```
(define (problem gripper-example)
	(:domain gripper-typed)
	(:objects
		ball1 ball2 ball3 ball4 ball5 ball6 - ball
		gripper-left gripper-right - gripper
		rooma roomb - room
	)
	(:init
		(at-robby rooma)
		(free gripper-left)
		(free gripper-right)
		(at ball1 rooma)
		(at ball2 rooma)
		(at ball3 rooma)
		(at ball4 rooma)
		(at ball5 rooma)
		(at ball6 rooma)
	)
	(:goal (and
		(at ball1 roomb)
		(at ball2 roomb)
		(at ball3 roomb)
		(at ball4 roomb)
		(at ball5 roomb)
		(at ball6 roomb)
	))
)
```

As you can see, you don't have to manually create all the problem objects (but you still can). pddlprinter does this job for you automatically by using information given in the planning domain. pddlprinter currently doesn't support a lot of features or complete type-inference, but it is work in progress.
