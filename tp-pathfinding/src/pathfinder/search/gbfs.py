from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class GreedyBestFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Greedy Best First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = root.cost

        # Initialize frontier with the root node
        frontier = PriorityQueueFrontier()
        frontier.add(root, grid.heuristic(root))

        while True:
            if frontier.is_empty():
                return NoSolution(reached)

            node = frontier.pop()
            if grid.objective_test(node.state):
                return Solution(node, reached)

            for action in grid.actions(node.state):
                new_state = grid.result(node.state, action)
                new_cost = node.cost + grid.individual_cost(node.state, action)
                if new_state not in reached or new_cost < reached[new_state]:
                    new_node = Node("", state=new_state, cost=new_cost, parent=node, action=action)
                    reached[new_state] = new_cost
                    frontier.add(new_node, grid.heuristic(new_node))

        return NoSolution(reached)
