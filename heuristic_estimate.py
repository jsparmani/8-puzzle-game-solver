class HeuristicEstimate(object):
    """Interface class: HeuristicFunction
    """
    def h(self, current_node, target_state):
        pass

class H1(HeuristicEstimate):
    def h(self, current_node, target_state):
        """counting the tiles out of place
           return the number of tiles that are out of place
        """
        count = 0
        for i in range(9):
            if current_node.state.data[i] != target_state.data[i]:
                count += 1
        return count

class H2(HeuristicEstimate):
    def h(self, current_node, target_state):
        """counting the tiles in place
           return the number of tiles that are in place
        """
        count = 0
        for i in range(9):
            if current_node.state.data[i] == target_state.data[i]:
                count += 1
        return count