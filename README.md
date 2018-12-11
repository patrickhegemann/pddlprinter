# PDDLPrinter

This is a Python3 module aimed at convenient generation of problems in PDDL for Automated Planning and is currently in early development.

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
