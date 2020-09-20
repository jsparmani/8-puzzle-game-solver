from solution import Solution
from search_method import DescentHillClimbing
from heuristic_estimate import *

class HillClimbingSolution(Solution):
	"""Searching with Descent Hill Climbing algorithm with Heuristic Function: G + H1
	"""
	__slot__ = {'method_name', 'heuristic_estimate'}

	def __init__(self, game_state_as_array):
		self.method_name = "Descent Hill Climbing"
		self.heuristic_estimate = "H1() Counting Misplaced Tiles"
		Solution.__init__(self, game_state_as_array)
		self.set_search_method(DescentHillClimbing(H1()))