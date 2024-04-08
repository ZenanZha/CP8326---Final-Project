from heapq import heappush, heappop
from AStar import astar
from utils import detect_conflict, CTNode, handle_conflicts

class MACBS:
  def __init__(self, environment, agents):
    self.environment = environment
    self.agents = agents
    self.root = CTNode(constraints=[])

  def search(self):
    open_set = [self.root]

    while open_set:
        node = open_set.pop(0)

        # Run A* for each agent with the current set of constraints
        paths = {agent.agent_id: astar(self.environment, agent.start, agent.goal, node.constraints) for agent in self.agents}

        for agent_id, path in paths.items():
            if not path:
                break
            print(f"Agent {agent_id} path: {path}")
        # Detect conflicts in the paths
        conflict = detect_conflict(self.environment, paths)

        if not conflict:
            # If no conflict, solution is found
            return paths
        
        # if conflict:
        #    handle_conflicts(conflict, node, open_set)

        print(f"Conflict detected: {conflict}")
        # If there is a conflict, branch the tree
        for agent_id, position, timestep in conflict:
            # Create a new CTNode for each conflict with updated constraints
            new_constraints = node.constraints.copy()
            new_constraints.append((agent_id, position, timestep))
            new_node = CTNode(constraints=new_constraints, parent=node)
            open_set.append(new_node)

    return None  # No solution found
