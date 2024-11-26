from flask import Flask, render_template, request, jsonify
import osmnx as ox
import networkx as nx
import time
app = Flask(__name__)

G = ox.graph_from_point((29.651634, -82.324826), dist=25000, network_type='drive')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/shortest_path", methods=["POST"])
def shortest_path():
    data = request.json
    point_A = tuple(data["pointA"])  # [lat, lon]
    point_B = tuple(data["pointB"])  # [lat, lon]

    node_A = ox.distance.nearest_nodes(G, point_A[1], point_A[0])  # lon, lat
    node_B = ox.distance.nearest_nodes(G, point_B[1], point_B[0])  # lon, lat

    # data to measure other than time? edges and nodes checked?
    start_shortest_path = time.time()
    shortest_path = nx.shortest_path(G, source=node_A, target=node_B, weight="length")
    end_shortest_path = time.time()

    start_dijkstra = time.time()
    dijkstras_path = nx.dijkstra_path(G, source=node_A, target=node_B, weight="length")
    end_dijkstra = time.time()

    start_bellman_ford = time.time()
    bellman_ford_path = nx.bellman_ford_path(G, source=node_A, target=node_B, weight="length")
    end_bellman_ford = time.time()

    shortest_path_time = end_shortest_path - start_shortest_path
    dijkstras_time = end_dijkstra - start_dijkstra
    bellman_ford_time = end_bellman_ford - start_bellman_ford

    shortest_path_coords = [(G.nodes[node]["y"], G.nodes[node]["x"]) for node in shortest_path]
    dijkstras_path_coords = [(G.nodes[node]["y"], G.nodes[node]["x"]) for node in dijkstras_path]
    bellman_ford_path_coords = [(G.nodes[node]["y"], G.nodes[node]["x"]) for node in bellman_ford_path]
    return jsonify({"path_shortest": shortest_path_coords, "path_dijkstras": dijkstras_path_coords, "path_bellman_ford": bellman_ford_path_coords, "time_shortest": shortest_path_time, "time_dijkstras": dijkstras_time, "time_bellman_ford": bellman_ford_time})

if __name__ == "__main__":
    app.run(debug=True)
