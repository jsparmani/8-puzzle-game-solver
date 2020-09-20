from solution import Solution
from search_method import BestFirstSearch
from heuristic_estimate import *

class BestFirstSearchSolution(Solution):
    """Searching with Best-First Search algorithm
    """
    __slot__ = {'method_name', 'heuristic_estimate'}
    
    def __init__(self, game_state_as_array):
        self.method_name = "Best-First-Search"
        self.heuristic_estimate = "H1() Counting Number of Misplaced Tiles"
        Solution.__init__(self, game_state_as_array)
        self.set_search_method(BestFirstSearch(H1()))