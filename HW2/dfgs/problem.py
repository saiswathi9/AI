from node import *

class Problem(object):

    """The abstract class for a formal problem. You should subclass
    this and implement the methods actions and result, and possibly
    __init__, goal_test, and path_cost. Then you will create instances
    of your subclass and solve them with the various search functions."""

    def __init__(self, initial, goal=None):
        """The constructor specifies the initial state, and possibly a goal
        state, if there is a unique goal. Your subclass's constructor can add
        other arguments."""
        self.initial = initial
        self.goal = goal
    
    def locationOfTile0(self, state):
        locOf0 = state.index(0)
        return locOf0
        
    def actions(self, state):
        """Return the actions that can be executed in the given
        state. The result would typically be a list, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once."""
        validActionsList = []
        locOf0InState = self.locationOfTile0(state)
        
        if locOf0InState in range(0,12):
            validActionsList.append('Down')
        if locOf0InState in range(4, 15):
            validActionsList.append('Up')
        if locOf0InState in [1,2,3,5,6,7,9,10,11,13,14,15]:
            validActionsList.append('Left')
        if locOf0InState in [0,1,2,4,5,6,8,9,10,12,13,14]:
            validActionsList.append('Right')
        return validActionsList

    def result(self, state, action):
        """Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state)."""
        self.locationOfTile0(state)
        resultantState = list(state)#The state was created as a tuple, and we need to make it a list to move it's contents around. We copy the current state into the new state and 
        dictLocChange = {'Up': -4, 'Down': 4, 'Left':-1, 'Right':1}
        swappedStateLocation = self.locationOfTile0(state) + dictLocChange[action]#Swapped state is new location of the new location of the blank tile. We need to copy it's content out and put blank there.
        swappedTile = resultantState[swappedStateLocation]
        resultantState[self.locationOfTile0(state)] = swappedTile
        resultantState[swappedStateLocation] = 0
        
        return tuple(resultantState)
        

    def goal_test(self, state):
        """Return True if the state is a goal. The default method compares the
        state to self.goal or checks for state in self.goal if it is a
        list, as specified in the constructor. Override this method if
        checking against a single self.goal is not enough."""
        if isinstance(self.goal, list):
            return is_in(state, self.goal)
        else:
            return state == self.goal

    def path_cost(self, c, state1, action, state2):
        """Return the cost of a solution path that arrives at state2 from
        state1 via action, assuming cost c to get up to state1. If the problem
        is such that the path doesn't matter, this function will only look at
        state2.  If the path does matter, it will consider c and maybe state1
        and action. The default method costs 1 for every step in the path."""
        return c + 1