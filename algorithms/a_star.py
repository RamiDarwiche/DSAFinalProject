import heapq
import math

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
    heapq.heappush(visited, (0, source))
    g_score = {source: 0}
    came_from = {}

    nodes_visited = 0
    edges_checked = 0

    while visited:
        _, current = heapq.heappop(visited)
        nodes_visited += 1

        if current == target:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(source)

            return path[::-1], edges_checked, nodes_visited

        for neighbor in G.neighbors(current):
            edge_weight = G.get_edge_data(current, neighbor)[0][weight]
            edges_checked += 1
            tentative_g_score = g_score[current] + edge_weight
            estimated_cost = heuristic(G, neighbor, target)
            f_score = tentative_g_score + estimated_cost

            if tentative_g_score < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                heapq.heappush(visited, (f_score, neighbor))