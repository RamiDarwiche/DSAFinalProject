import heapq

def dijkstra_osmnx(G, source, target, weight="length"):
    # Creates priority queue to hold unvisited nodes
    # Adds source node
    unvisited_nodes = []
    heapq.heappush(unvisited_nodes, (0, source))

    # Sets distance for source node to 0 and other nodes to infinity
    distance = {node: float("inf") for node in G.nodes}
    distance[source] = 0

    # Keeping track of the previous node in the path to each node
    # Set all to None at first
    previous_nodes = {node: None for node in G.nodes}

    # While nodes still need to be visited
    while unvisited_nodes:
        # Remove node from queue
        current_distance, current_node = heapq.heappop(unvisited_nodes)

        # If node's distance is greater than recorded distance then do nothing
        if current_distance > distance[current_node]:
            continue

        # For all neighbors, if weight of edge + distance < recorded:
        # Update recorded distance and previous node
        # Add neighbor to queue to be visited
        for u, v, data in G.edges(data=True):
            dist = current_distance + data.get(weight, float("inf"))

            if dist < distance[v]:
                distance[v] = dist
                previous_nodes[v] = current_node
                heapq.heappush(unvisited_nodes, (dist, v))

    # Returns shortest path found from the source node to the target node
    path = []
    current = target
    while current is not None:
        path.append(current)
        current = previous_nodes[current]
    path.reverse()

    return path
