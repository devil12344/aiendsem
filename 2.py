import heapq

# Structure to represent a node in the graph
class Node:
    def __init__(self, index, g_cost, h_cost):
        self.index = index  # Index of the node
        self.g_cost = g_cost  # Cost from start node to this node
        self.h_cost = h_cost  # Heuristic cost (estimated cost from this node to goal node)
        self.f_cost = g_cost + h_cost  # f(n) = g(n) + h(n)

    # Custom comparison method for priority queue
    def __lt__(self, other):
        return self.f_cost < other.f_cost

# A* algorithm function
def AStar(graph, heuristic, start, goal):
    n = len(graph)

    # Priority queue to store nodes to be explored, ordered by f_cost
    open_list = []

    # Add the start node to the open list
    heapq.heappush(open_list, Node(start, 0, heuristic[start]))

    # Set to keep track of visited nodes
    visited = set()

    while open_list:
        # Get the node with the lowest f_cost from the open list
        current = heapq.heappop(open_list)

        # Check if the current node is the goal
        if current.index == goal:
            return current.g_cost

        # Mark current node as visited
        visited.add(current.index)

        # Expand current node
        for neighbor in range(n):
            # Check if there is a connection from current node to neighbor and neighbor is not visited
            if graph[current.index][neighbor] != 0 and neighbor not in visited:
                g_cost = current.g_cost + graph[current.index][neighbor]
                h_cost = heuristic[neighbor]
                f_cost = g_cost + h_cost

                # Add neighbor to open list
                heapq.heappush(open_list, Node(neighbor, g_cost, h_cost))

    # If goal node is not reachable
    return -1

# Main function
def main():
    n = int(input("Enter the number of nodes: "))
    graph = []

    print("Enter the adjacency matrix:")
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    heuristic = list(map(int, input("Enter the heuristic values for each node: ").split()))

    start = int(input("Enter the start node: "))
    goal = int(input("Enter the goal node: "))

    shortest_path_cost = AStar(graph, heuristic, start, goal)

    if shortest_path_cost == -1:
        print(f"No path found from node {start} to node {goal}")
    else:
        print(f"Shortest path cost from node {start} to node {goal} is: {shortest_path_cost}")

if __name__ == "__main__":
    main()
