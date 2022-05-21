# PDDLPrinter

PDDLPrinter is a Python module for convenient generation of planning problem instances for automated planning as PDDL, which can be used as input to any standard off-the-shelf planner. It provides a lightweight interface and makes sure to generate valid PDDL according to the given problem specification. Where possible, missing parts of the specification are automatically inferred from the domain definition and the given constraints.

## Features

* [x] Parsing PDDL domain file to infer object types, constants and predicates for use in problem generation
* [x] Initialization of predicates
* [x] Conjunctive goals
* [x] Automatic declaration of the used objects

Experimental Features:
* [x] Specification of a metric in the form of a single function
* [x] Initialization of numeric fluents
* [x] Automatic object declaration and (partly) type inference

Roadmap:
* [ ] Full support of PDDL features, such as
	* Goals of arbitrary logical structure
	* Derived predicates
	* Specification of metrics with arbitrary structure
* [ ] Fully automatic type inference for object declaration
* [ ] Convenience functions for higher-level problem specification and automatic generation of object structures such as ordered sets, grids, graphs, ...


## Installation (pip)

Clone this repository and [install it from source](https://packaging.python.org/tutorials/installing-packages/#installing-from-a-local-src-tree):
```shell
git clone https://github.com/patrickhegemann/pddlprinter.git
cd pddlprinter
pip install .
```

## Usage Example

Here is an example script that generates a classic "Gripper" planning problem instance with 2 rooms containing 6 balls in total.

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
    problem.init("at", f"ball{i}", "rooma")
    problem.goal("at", f"ball{i}", "roomb")

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
