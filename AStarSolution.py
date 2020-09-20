from solution import Solution
from search_method import AStar
from heuristic_estimate import *

class AStarSolution(Solution):
	"""Searching with A* algorithm with Heuristic Function: G + H1
	"""
	__slot__ = {'method_name', 'heuristic_estimate'}

	def __init__(self, game_state_as_array):
		self.method_name = "A*"
		self.heuristic_estimate = "H2()     (Counting Placed Tiles)"
		Solution.__init__(self, game_state_as_array)
		self.set_search_method(AStar(H2()))