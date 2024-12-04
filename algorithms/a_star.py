import heapq
import math

# Heuristic function
# This function will take the current node and target node, and find the Euclidean distance between them
def heuristic (G, current, target):
    node_data_current = G.nodes[current]
    nearest_lat_current = node_data_current['y']
    nearest_lon_current = node_data_current['x']

    node_data_target = G.nodes[target]
    nearest_lat_target = node_data_target['y']
    nearest_lon_target = node_data_target['x']

    dx = nearest_lon_target - nearest_lon_current
    dy = nearest_lat_target - nearest_lat_current
    distance = math.sqrt(dx ** 2 + dy ** 2)

    return distance

def astar_path_osmnx(G, source, target, heuristic, weight='length'):

    visited = []

    # Pushes into visited the priority (left part of the pair) and the node (right part of the pair).
    heapq.heappush(visited, (0, source))

    g_score = {source: 0}
    came_from = {}

    # Keeps track of the nodes and edged visited/checked.
    nodes_visited = 0
    edges_checked = 0

    # While visited isn't empty yet
    while visited:
        _, current = heapq.heappop(visited)
        nodes_visited += 1

        # What to do if we find our final destination
        if current == target:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(source)

            # Return function of the path took
            return path[::-1], edges_checked, nodes_visited

        # Each node is visited and will check all its neighbors
        for neighbor in G.neighbors(current):
            edge_weight = G.get_edge_data(current, neighbor)[0][weight]
            edges_checked += 1
            tentative_g_score = g_score[current] + edge_weight
            estimated_cost = heuristic(G, neighbor, target)
            f_score = tentative_g_score + estimated_cost

            # Decides which path to take and loops back
            if tentative_g_score < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                heapq.heappush(visited, (f_score, neighbor))