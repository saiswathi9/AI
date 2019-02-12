
#Reference https://github.com/aimacode/aima-python/blob/master/search.py

from node import *
import time
import problem


def depth_first_graph_search(problem):
    #Search the deepest nodes in the search tree first.
     #   Search through the successors of a problem to find a goal.
      #  The argument frontier should be an empty queue.
       # Does not get trapped by loops.
        #If two paths reach a state, only use the first one. [Figure 3.7]
    start = time.time()
    nodeExploredCount = 0 
    frontier = [(Node(problem.initial))]  # Sick storing for nodes explore.
    explored = set() #Create a set to store states we've explored previously
    while frontier:
        node = frontier.pop()
        nodeExploredCount +=1
        #print nodeExploredCount
        if problem.goal_test(node.state):#Test a node to see if it is the goal state. If it is, then we can return that node as well as all relevant statistics
            stop = time.time()
            print("We've expanded ", len(explored), " Nodes")
            print('Time: ', float(stop -start) *1000)
			#print(node.solution, "Is the solution to the graph")
			#print(node.path, "Is the path from the shuffled board to the goal board/n", "Note that the move suggested is to be done on the blank tile")
            return node
        
        if len(explored)>=1000000:#1 million nodes expanded
            stop = time.time() 
            print("Node expanded greater than 1 million")
            print('Time: ', float(stop - start)*1000)
            break
        
        if(node.state not in explored):#Add nodes to the frontier if the node hasn't been explored or isn't already in the frontier.
            frontier.extend(node.expand(problem))
            explored.add(node.state) #Add the node to the set of explored nodes since we're implementing a graph search. This ensures we don't search that node again. 
    return None
