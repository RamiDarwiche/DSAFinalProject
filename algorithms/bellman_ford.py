from collections import defaultdict

def bellman_ford_osmnx(G, source, target, weight="length"):

    # initialize distances to infinity
    distances = defaultdict(lambda: float('inf'))
    previous_nodes = defaultdict(lambda: None)
    distances[source] = 0 # set source node distance to 0

    nodes_visited = 0
    edges_checked = 0

    # relax V-1 edges
    for _ in range(len(G) - 1):
        updated = False

        #  iterate through all nodes
        for node in G:
            nodes_visited += 1

            # iterate through all neighbors of current node
            for neighbor in G.neighbors(node):
                edge_weight = G.get_edge_data(node, neighbor)[0][weight] # get weight
                edges_checked += 1

                # calculate new potential distance
                new_distance = distances[node] + edge_weight\

                # if path is more optimal, relax edge/update distance to optimal path
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous_nodes[neighbor] = node
                    updated = True

        # break early is no updates
        if not updated:
            break

    # check for negative edge cycles by relaxing edges an additional time
    for node in G:
        for neighbor in G.neighbors(node):
            edge_weight = G.get_edge_data(node, neighbor)[0][weight]
            if distances[node] + edge_weight < distances[neighbor]:
                raise ValueError("Negative weight cycle") # alert if negative weight cycle is found

    # reconstruct shortest path from target to source and reverse
    path = []
    current_node = target
    while current_node is not None:
        path.append(current_node)
        current_node = previous_nodes[current_node]
    path.reverse()

    # if no path found, we are cooked
    if distances[target] == float('inf'):
        return [], edges_checked, nodes_visited

    # return shortest path, number of edges and nodes checked
    return path, edges_checked, nodes_visited
