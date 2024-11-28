network_map = {
    "X": ["Y", "Z"],
    "Y": ["A", "B"],
    "Z": ["C"],
    "A": [],
    "B": ["C"],
    "C": []
}

def bfs_traversal(network, start_point):
    explored = []  # List to keep track of visited nodes
    queue_list = []  # Queue to manage traversal

    # Initialize the BFS process with the start point
    explored.append(start_point)
    queue_list.append(start_point)

    print("Breadth-First Search Path:")
    while queue_list:
        # Remove the first node from the queue and process it
        current = queue_list.pop(0)
        print(current, end=" ")

        # Check and enqueue unvisited neighbors
        for adjacent in network[current]:
            if adjacent not in explored:
                explored.append(adjacent)
                queue_list.append(adjacent)

# Perform BFS starting from node 'X'
bfs_traversal(network_map, "X")
