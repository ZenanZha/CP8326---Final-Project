from MAPF import MACBS
from utils import Agent

def main():
    # Define your grid environment: 0 for free space, 1 for obstacles
    environment = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 1, 1, 0]
    ]

    # Define your agents with unique IDs, start, and goal positions
    agents = [
        Agent(agent_id=1, start=(0, 0), goal=(4, 4)),
        Agent(agent_id=2, start=(4, 4), goal=(0, 0))
        # Add more agents as needed
    ]

    # Instantiate the MACBS algorithm
    macbs = MACBS(environment, agents)

    # Run the MACBS search
    solution = macbs.search()

    # Print the solution
    if solution:
        print("Solution paths for each agent:")
        for agent_id, path in solution.items():
            print(f"Agent {agent_id}: {path}")
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
