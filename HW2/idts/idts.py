from node import *
import problem
import time
import sys

#I get an overflow error using this methods. I use DFS instead.
def depth_limited_search(problem, limit=50):
    #"[Figure 3.17]"
    def recursive_dls(node, problem, limit):
        if problem.goal_test(node.state):
            return node
        elif limit == 0:
            return 'cutoff'
        else:
            cutoff_occurred = False
            for child in node.expand(problem):
                result = recursive_dls(child, problem, limit - 1)
                if result == 'cutoff':
                    cutoff_occurred = True
                elif result is not None:
                    return result
            return 'cutoff' if cutoff_occurred else None

    # Body of depth_limited_search:
    return recursive_dls(Node(problem.initial), problem, limit)

"""
def iterative_deepening_search1(problem):
    #"[Figure 3.18]"
    start = time.time()
    for depth in range(sys.maxsize):
        result = depth_limited_search(problem, depth)
        if depth >= 3:
            stop = time.time()
            print("1000000 nodes expanded")
            print("Time taken = ", float(start - stop)*1000)
            return None
        if result != 'cutoff':
            stop = time.time()
            print("Time taken = ", float(start - stop)*1000)
            return result
"""

def iterative_deepening_search(problem):
     #Search the nodes until a particular length in the search tree first.
     #Search through the successors of a problem to find a goal.
     #   The argument frontier should be an empty queue.
     #   Repeats infinitely in case of loops. [Figure 3.7]
    nodeExploredCount = 0
    start = time.time()
    for i in range(1, 1000000):
        frontier = [Node(problem.initial)]  # Stack
        while frontier:
            node = frontier.pop()
            if problem.goal_test(node.state):
                stop = time.time()
                print("We've expanded ", nodeExploredCount," Nodes", 'Time: ', float(stop -start) *1000,"ms")
                return node
                print nodeExploredCount
            if nodeExploredCount >=1000000:#1 million nodes expanded
                stop = time.time() 
                print("Node expanded greater than 1 million")
                print('Time: ', float(stop - start)*1000)
                return -1 #I use this to exit the program as break isn't working.
                break
                
            
            if node.depth < i:
                nodeExploredCount+=1
                frontier.extend(node.expand(problem))
    return None

