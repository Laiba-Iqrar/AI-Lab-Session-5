network = {
    "A": ["B", "D"],
    "B": ["E", "C"],
    "D": ["F"],
    "E": [],
    "C": ["F"],
    "F": []
}

explored = set()  # Set to store explored nodes
stack = []        # Stack for DFS processing

def depth_first_search(explored, network, start):
    if start not in explored:
        print(start)
        explored.add(start)
        for adjacent in network[start]:
            depth_first_search(explored, network, adjacent)

# Main Code
print("Depth-First Search Traversal:")
depth_first_search(explored, network, "A")
