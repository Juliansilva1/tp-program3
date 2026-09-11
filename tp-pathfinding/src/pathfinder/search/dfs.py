from ..models.grid import Grid
from ..models.frontier import StackFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class DepthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Depth First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)
        
        if grid.objective_test(root.state):
            return Solution(root, {})

        frontier = StackFrontier()
        frontier.add(root)

        # Initialize expanded with the empty dictionary
        expanded = dict()

        while True:
            if frontier.is_empty():
                return NoSolution(expanded)

            node = frontier.remove()

            if node.state in expanded:
                continue
            expanded[node.state] = True
            for action in grid.actions(node.state):
                new_state = grid.result(node.state, action)
                if new_state not in expanded:
                    new_node = Node('', new_state, node.cost + grid.individual_cost(node.state, action), node, action)
                    if grid.objective_test(new_state):
                        return Solution(new_node, expanded)
                    frontier.add(new_node)

        return NoSolution(expanded)
