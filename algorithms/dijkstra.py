import heapq

def dijkstra_osmnx(G, source, target, weight="length"):
    # Creates priority queue to hold unvisited nodes
    # Adds source node
    unvisited_nodes = [(0, source)]

    # Sets distance for source node to 0 and other nodes to infinity
    distances = {node: float('inf') for node in G}
    distances[source] = 0

    # Keeping track of the previous node in the path to each node
    # Set all to None at first
    previous_nodes = {node: None for node in G}
    visited = set()

    nodes_visited = 0
    edges_checked = 0

    # While nodes still need to be visited
    while unvisited_nodes:
        # Remove node from queue
        current_distance, current_node = heapq.heappop(unvisited_nodes)

        # If node visited, skip iteration
        if current_node in visited:
            continue

        visited.add(current_node)
        nodes_visited += 1

        # For all neighbors, if weight of edge + distance < recorded:
        # Update recorded distance and previous node
        # Add neighbor to queue to be visited
        for neighbor in G.neighbors(current_node):
            new_distance = current_distance + G.get_edge_data(current_node, neighbor)[0][weight]
            edges_checked += 1
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(unvisited_nodes, (new_distance, neighbor))

    # Returns shortest path found from the source node to the target node, also returns number of nodes and edges visited
    path = []
    current_node = target
    while current_node is not None:
        path.append(current_node)
        current_node = previous_nodes[current_node]
    path.reverse()

    return path, edges_checked, nodes_visited