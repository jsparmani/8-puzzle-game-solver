import time
import random
from game_tree_node import GameTreeNode

class SearchMethod(object):
    """Interface class: SearchMethod
    """
    def search(self, initial_node, target_state):
        pass
    

class BFS(SearchMethod):
    """Breadth-First Search Algorithm
    """
    
    def search(self, initial_node, target_state):
        """Search for the target state
		   return target_node as a GameTreeNode object and elapsed_time in second
		"""
        target_node = None
        start = time.time()
        Open = [initial_node]
        visited_nodes = [initial_node]
        while Open:
            current_node = Open.pop(0)
            if current_node.state.data == target_state.data:
                target_node = current_node
                break
            else:
                current_node.generate_children()
                if current_node.children != None:
                    for child in current_node.children:
                        flag = 0
                        for node in visited_nodes:
                            if node.state.data == child.state.data:
                                flag = 1
                        if flag == 0:
                            Open.append(child)
                            visited_nodes.append(child)
        end = time.time()
        elapsed_time = end - start
        return target_node, elapsed_time