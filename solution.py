from game_tree_node import GameTreeNode
from game_state import EightPuzzleGameState

class Solution(object):
    """Finding the solution of the game.
       _initial_node which is an instance of GameTreeNode represent the initial node
       _target_state which is an instance of EightPuzzleGameState represent the target state
       _solution_path which is a list of GameTreeNode from initial node to the target node
       _elapsed_time contains the time(sec) a sepcific algorithm spent to find the target node
    """
 
    __slots__= {'_initial_node', '_target_state', '_solution_path', '_elapsed_time', '_target_node'}
    
    def __init__(self, game_state_as_array):
        self._initial_node = GameTreeNode(game_state_as_array, None)
        self._target_state = EightPuzzleGameState(['1', '2', '3', '4', '5', '6', '7', '8', 'x'])
        self._solution_path = []
        self._elapsed_time = None
        self._target_node = None
        
    def set_search_method(self, search_method):
        self.search_method = search_method
        
    def perform_search_method(self):
        self._target_node, self._elapsed_time = self.search_method.search(self._initial_node, self._target_state)
    
    def count_step(self):
        """return the number of steps from begining to the target node
        """

        if self._target_node:
            current_node = self._target_node
            while current_node.state.data != self._initial_node.state.data:
                self._solution_path.append(current_node.state.representation)
                current_node = current_node.parent
            self._solution_path.append(self._initial_node.state.representation)
            return len(self._solution_path) - 1
        else:
            return 0
        
    @property
    def initial_node(self):
        """Gets the initial node"""
        return self._initial_node

    @property
    def target_state(self):
        """Gets the target state for this game"""
        return self._target_state

    @property
    def solution_path(self):
        """Gets nodes of the solution path"""
        return self._solution_path

    @property
    def elapsed_time(self):
        """Gets the elapsed time"""
        return self._elapsed_time

    @property
    def target_node(self):
        """Gets the target node"""
        return self._target_node
        