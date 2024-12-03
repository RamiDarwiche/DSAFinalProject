import heapq

def dijkstra_osmnx(G, source, target, weight="length"):

    unvisited_nodes = [(0, source)]  # Start with source node and distance 0

    distances = {node: float('inf') for node in G}
    distances[source] = 0
    previous_nodes = {node: None for node in G}
    visited = set()

    nodes_visited = 0
    edges_checked = 0

    while unvisited_nodes:
        current_distance, current_node = heapq.heappop(unvisited_nodes)

        if current_node in visited:
            continue

        visited.add(current_node)
        nodes_visited += 1

        for neighbor in G.neighbors(current_node):
            new_distance = current_distance + G.get_edge_data(current_node, neighbor)[0][weight]
            edges_checked += 1
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(unvisited_nodes, (new_distance, neighbor))

    path = []
    current_node = target
    while current_node is not None:
        path.append(current_node)
        current_node = previous_nodes[current_node]
    path.reverse()

    return path, edges_checked, nodes_visited