from problem import *
from idts import *

#Define the 2 test state
test1Tuple = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,0,15)

#test1Tuple = (1,2,3,4,5,6,7,8,9,10,11,12,13,0,14,15)

#test2Tuple = (1,2,3,4,5,6,7,8,9,10,11,0,13,14,15, 12)

#Unsolvable tuples
test2Tuple = (1,3,2,4,5,6,7,8,9,10,11,12,13,14,15)

#test1Tuple = (1, 2, 7, 3, 5, 6, 11, 4, 9, 10, 15, 8, 13, 14, 12, 0 ) #Actual problems
"""
	1, 2, 7, 3,
    5, 6, 11, 4,
    9, 10, 15, 8,
    13, 14, 12, 0

"""
#test2Tuple = (5, 1, 7, 3, 9, 2, 11, 4, 13, 6, 15, 8, 0, 10, 14, 12) #Actual problems
"""
	5, 1, 7, 3,
    9, 2, 11, 4,
    13, 6, 15, 8,
    0, 10, 14, 12
"""
#Define the goal state
goalTuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0)
"""
	1, 2, 3, 4,
    5, 6, 7, 8,
    9, 10, 11, 12,
    13, 14, 15, 0
"""

problem1 = problem.Problem(test1Tuple, goalTuple)
problem2 = problem.Problem(test2Tuple, goalTuple)

node = iterative_deepening_search(problem1)
if(node):
	print(node.solution())
	print("\n")
else:
	print("Not solvable in this implementation")
	print("\n")
	
node = iterative_deepening_search(problem2)
if(node):
	print(node.solution())
	print("\n")
else:
	print("Not solvable in this implementation")
	print("\n")