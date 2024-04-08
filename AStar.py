from utils import Node, get_children_with_constraints, update_node_costs, construct_path
import heapq

def astar(maze, start, end, constraints):
    start_node = Node(None, start)
    end_node = Node(None, end)

    open_set = []
    heapq.heappush(open_set, start_node)
    closed_set = set()

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node == end_node:
            return construct_path(current_node)

        closed_set.add(current_node)

        for child in get_children_with_constraints(current_node, maze, constraints):
            if child in closed_set:
                continue

            update_node_costs(child, current_node, end_node)

            if not any(child == open_node and child.g > open_node.g for open_node in open_set):
                heapq.heappush(open_set, child)

    return None  # No path found
