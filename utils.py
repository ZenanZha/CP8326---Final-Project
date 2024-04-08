class CTNode:
  def __init__(self, constraints, parent=None):
    self.constraints = constraints
    self.parent = parent
    self.children = []
    self.cost = 0

  def add_child(self, child_node):
    self.children.append(child_node)

class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

    def __lt__(self, other):
        return self.f < other.f
    
    def __hash__(self):
        return hash(self.position)

class Agent:
  def __init__(self, start, goal):
    self.start = start
    self.goal = goal
    self.current_pos = start
    self.path = None

def heuristic(pos, goal):
    # Manhattan distance heuristic
    return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])

def get_children(node, maze):
    children = []
    for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:  # Adjacent squares
        node_position = (node.position[0] + new_position[0], node.position[1] + new_position[1])
        if 0 <= node_position[0] < len(maze) and 0 <= node_position[1] < len(maze[0]) and maze[node_position[0]][node_position[1]] == 0:
            new_node = Node(node, node_position)
            children.append(new_node)
    return children

def update_node_costs(child, current_node, end_node):
    child.g = current_node.g + 1
    child.h = heuristic(child.position, end_node.position)
    child.f = child.g + child.h

def construct_path(current_node):
    path = []
    while current_node is not None:
        path.append(current_node.position)
        current_node = current_node.parent
    return path[::-1]

def get_valid_neighbors(pos, environment, constraints):
  # Get valid neighbors considering obstacles and constraints
  neighbors = [(pos[0] + 1, pos[1]), (pos[0] - 1, pos[1]), (pos[0], pos[1] + 1), (pos[0], pos[1] - 1)]
  valid_neighbors = []
  for neighbor in neighbors:
    if 0 <= neighbor[0] < len(environment) and 0 <= neighbor[1] < len(environment[0]) and environment[neighbor[0]][neighbor[1]] != 1:
      # Check for obstacles (environment[neighbor[0]][neighbor[1]] != 1)
      if all(neighbor not in constraint for constraint in constraints):
        valid_neighbors.append(neighbor)
  return valid_neighbors

def detect_conflict(environment, paths):
    # Improved conflict detection
    conflicts = []

    # Get all agent IDs (or keys) from paths
    agent_ids = list(paths.keys())

    # Ensure we have at least two paths to compare
    if len(agent_ids) < 2:
        return conflicts

    print(f"Agent IDs: {agent_ids}")
    print(f"Paths: {paths}")
    print(f"Paths[0]: {[len(paths[agent_id]) for agent_id in agent_ids if paths[agent_id]]}")
    min_path_length = min(len(paths[agent_id]) for agent_id in agent_ids if paths[agent_id])

    for i in range(len(agent_ids)):
        for j in range(i + 1, len(agent_ids)):
            agent_i = agent_ids[i]
            agent_j = agent_ids[j]

            # Check if both agents have paths
            if not paths[agent_i] or not paths[agent_j]:
                continue

            for t in range(min_path_length):
                if t >= len(paths[agent_i]) or t >= len(paths[agent_j]):
                    break

                if paths[agent_i][t] == paths[agent_j][t]:
                    # Exclude conflicts at start or goal positions
                    if paths[agent_i][t] not in {paths[agent_i][0], paths[agent_i][-1], paths[agent_j][0], paths[agent_j][-1]}:
                        conflicts.append((agent_i, agent_j, paths[agent_i][t]))

    return conflicts


# utils.py

class Agent:
    def __init__(self, agent_id, start, goal):
        self.agent_id = agent_id  # Unique identifier for the agent
        self.start = start        # Starting position (tuple of coordinates)
        self.goal = goal          # Goal position (tuple of coordinates)

    def __str__(self):
        return f"Agent {self.agent_id}: Start {self.start}, Goal {self.goal}"


def get_children_with_constraints(node, maze, constraints):
    children = []
    for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:  # Adjacent squares
        node_position = (node.position[0] + new_position[0], node.position[1] + new_position[1])
        if not is_valid_position(node_position, maze, constraints):
            continue
        new_node = Node(node, node_position)
        children.append(new_node)
    return children

def is_valid_position(position, maze, constraints):
    if position[0] < 0 or position[0] >= len(maze) or position[1] < 0 or position[1] >= len(maze[0]):
        return False
    if maze[position[0]][position[1]] == 1:  # Check for obstacles
        return False
    # if any(position == constraint[2] for constraint in constraints):  # Check for conflicts
    #     return False
    if position in [constraint[2] for constraint in constraints]:  # Check for constraints
        return False
    return True


def handle_conflicts(conflicts, node, open_set):
    for agent_id, position, timestep in conflicts:
        # Copy the existing constraints and add the new constraint for the current conflict
        new_constraints = node.constraints.copy()
        new_constraint = (agent_id, position, timestep)
        
        # Check if this constraint already exists to avoid repeating the same state
        if new_constraint not in new_constraints:
            new_constraints.append(new_constraint)
            
            # Create a new CTNode with updated constraints
            new_node = CTNode(constraints=new_constraints, parent=node)
            
            # TODO: Recalculate paths for the agents considering the new constraints
            # Ensure that paths are actually different and the conflict is resolved

            # Add the new node to the open set if it represents a new state
            open_set.append(new_node)
        else:
            # Constraint already exists, indicating a potential loop or redundant path
            print(f"Skipping redundant constraint: {new_constraint}")
