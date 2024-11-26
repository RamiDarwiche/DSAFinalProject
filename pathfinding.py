"""
TODO:
    1: get graph information from openstreetmap API, intersections are nodes and streets are edges
    2: design graph pathfinding algorithms
    3: create api for interfacing with arbitrary geolocation on web browser map
"""

import heapq

# def dijkstra(graph, start):
#     priority_queue = []
#     heapq.heappush(priority_queue, (0, start))  # (distance, node)
#
#     distances = {node: float('inf') for node in graph}
#     distances[start] = 0
#
#     previous_nodes = {node: None for node in graph}
#
#     while priority_queue:
#         current_distance, current_node = heapq.heappop(priority_queue)
#
#         if current_distance > distances[current_node]:
#             continue
#
#         for neighbor, weight in graph[current_node].items():
#             distance = current_distance + weight
#
#             if distance < distances[neighbor]:
#                 distances[neighbor] = distance
#                 previous_nodes[neighbor] = current_node
#                 heapq.heappush(priority_queue, (distance, neighbor))
#
#     return distances, previous_nodes
#
#
import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt

# Define the starting and ending points (latitude, longitude)
point_A = (29.651634, -82.324826)  # Example: Gainesville, Florida
point_B = (29.648590, -82.343221)  # Another point in Gainesville

# Download the street network for the area around the points
G = ox.graph_from_point(point_A, dist=4000, network_type='drive', retain_all=True, truncate_by_edge=True)  # Adjust 'dist' for the area size

# Find the nearest nodes in the graph to the points
node_A = ox.distance.nearest_nodes(G, point_A[1], point_A[0])  # lon, lat
node_B = ox.distance.nearest_nodes(G, point_B[1], point_B[0])  # lon, lat

# Find the shortest path between the two nodes
shortest_path = nx.dijkstra_path(G, source=node_A, target=node_B, weight='length')

# Extract the subgraph for the shortest path
subgraph = G.subgraph(shortest_path)

# Plot the full graph and the shortest path
fig, ax = plt.subplots(figsize=(10, 10))
ox.plot_graph(G, ax=ax, show=False, close=False, node_size=10, edge_color="lightgray")
ox.plot_graph(subgraph, ax=ax, node_color="red", edge_color="blue", node_size=30, edge_linewidth=2)
plt.show()

# Optional: Convert the subgraph to GeoDataFrames for further processing
nodes, edges = ox.graph_to_gdfs(subgraph)
print("\nSubgraph nodes:")
print(nodes.head())
print("\nSubgraph edges:")
print(edges.head())


print(f"Shortest path from A to B (nodes): {shortest_path}")
