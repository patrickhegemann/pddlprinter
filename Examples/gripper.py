#!/usr/bin/python3

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
