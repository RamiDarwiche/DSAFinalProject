from collections import defaultdict

def bellman_ford_osmnx(G, source, target, weight="length"):
    distances = defaultdict(lambda: float('inf'))
    previous_nodes = defaultdict(lambda: None)
    distances[source] = 0

    nodes_visited = 0
    edges_checked = 0

    for _ in range(len(G) - 1):
        updated = False

        for node in G:
            nodes_visited += 1

            for neighbor in G.neighbors(node):
                edge_weight = G.get_edge_data(node, neighbor)[0][weight]
                edges_checked += 1

                new_distance = distances[node] + edge_weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous_nodes[neighbor] = node
                    updated = True

        if not updated:
            break

    for node in G:
        for neighbor in G.neighbors(node):
            edge_weight = G.get_edge_data(node, neighbor)[0][weight]
            if distances[node] + edge_weight < distances[neighbor]:
                raise ValueError("Negative weight cycle")

    path = []
    current_node = target
    while current_node is not None:
        path.append(current_node)
        current_node = previous_nodes[current_node]
    path.reverse()

    if distances[target] == float('inf'):
        return [], edges_checked, nodes_visited

    return path, edges_checked, nodes_visited
