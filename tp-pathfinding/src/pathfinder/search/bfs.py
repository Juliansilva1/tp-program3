from ..models.grid import Grid
from ..models.frontier import QueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class BreadthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Breadth First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        if grid.objective_test(root.state):
            return Solution(root, {})

        frontier = QueueFrontier()
        frontier.add(root)

        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = True

        while True:
            if frontier.is_empty():
                return NoSolution(reached)

            node = frontier.remove()
            for action in grid.actions(node.state):
                new_state = grid.result(node.state, action)
                if new_state not in reached:
                    new_node = Node('', new_state, node.cost + grid.individual_cost(node.state, action), node, action, )
                    if grid.objective_test(new_state):
                        return Solution(new_node, reached)
                    reached[new_state] = True
                    frontier.add(new_node)
                    
        return NoSolution(reached)
