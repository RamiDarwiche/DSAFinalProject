import heapq
import math
from cmath import sqrt

import osmnx as ox
import networkx as nx
import inspect

point_A = (29.651634, -82.324826)  # Example: Gainesville, Florida
point_B = (29.648590, -82.343221)  # Another point in Gainesville
G = ox.graph_from_point(point_A, dist=4000, network_type='drive', retain_all=True, truncate_by_edge=True)  # Adjust 'dist' for the area size

node_A = ox.distance.nearest_nodes(G, point_A[1], point_A[0])  # lon, lat
node_B = ox.distance.nearest_nodes(G, point_B[1], point_B[0])  # lon, lat

def heuristic (current, target):
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

    while visited:
        _, current = heapq.heappop(visited)

        if current == target:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(source)
            return path[::-1]

        for neighbor in G.neighbors(current):
            edge_weight = G[current][neighbor].get(weight, 1)
            tentative_g_score = g_score[current] + edge_weight
            estimated_cost = heuristic(neighbor, target)
            f_score = tentative_g_score + estimated_cost

            if tentative_g_score < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                heapq.heappush(visited, (f_score, neighbor))

    raise nx.NetworkXNoPath(f"No path between {source} and {target}.")

print(astar_path_osmnx(G, node_A, node_B, heuristic, weight='length'))
