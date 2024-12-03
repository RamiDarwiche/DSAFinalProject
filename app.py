import time
import osmnx as ox
from flask import Flask, render_template, request, jsonify
from algorithms.dijkstra import dijkstra_osmnx
from algorithms.a_star import astar_path_osmnx, heuristic
from algorithms.bellman_ford import bellman_ford_osmnx

app = Flask(__name__)

# initialize osmnx graph to include Gainesville
G = ox.graph_from_point((29.651634, -82.324826), dist=25000, network_type='drive')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/shortest_path", methods=["POST"])
def shortest_path():
    app.logger.info('Received POST request')
    try:
        # convert data from server request into library-friendly format
        data = request.json
        point_A = tuple(data["pointA"])  # [lat, lon]
        point_B = tuple(data["pointB"])

        # select graph nodes closest to the marker placements on map
        node_A = ox.distance.nearest_nodes(G, point_A[1], point_A[0])  # lon, lat
        node_B = ox.distance.nearest_nodes(G, point_B[1], point_B[0])

        # run algorithm 1, record time to run
        start_a_star = time.time()
        a_star_path, a_star_edge_count, a_star_node_count = astar_path_osmnx(G, source=node_A, target=node_B, heuristic=heuristic)
        end_a_star = time.time()

        # run algorithm 2, record time to run
        start_dijkstra = time.time()
        dijkstras_path, dijkstras_edge_count, dijkstras_node_count = dijkstra_osmnx(G, source=node_A, target=node_B, weight="length")
        end_dijkstra = time.time()

        # run algorithm 3, record time to run
        start_bellman_ford = time.time()
        bellman_ford_path, bellman_ford_edge_count, bellman_ford_node_count = bellman_ford_osmnx(G, source=node_A, target=node_B, weight="length")
        end_bellman_ford = time.time()

        # calculate runtimes for each algorithm
        a_star_time = end_a_star - start_a_star
        dijkstras_time = end_dijkstra - start_dijkstra
        bellman_ford_time = end_bellman_ford - start_bellman_ford

        # create a list of coordinates based on each algorithm's returned path
        a_star_coords = [(G.nodes[node]["y"], G.nodes[node]["x"]) for node in a_star_path]
        dijkstras_path_coords = [(G.nodes[node]["y"], G.nodes[node]["x"]) for node in dijkstras_path]
        bellman_ford_path_coords = [(G.nodes[node]["y"], G.nodes[node]["x"]) for node in bellman_ford_path]
        app.logger.info(a_star_edge_count)

        # convert data into JSON and return as response to index.html
        return jsonify({"path_a_star": a_star_coords, "path_dijkstras": dijkstras_path_coords, "path_bellman_ford": bellman_ford_path_coords, "time_a_star": a_star_time, "time_dijkstras": dijkstras_time, "time_bellman_ford": bellman_ford_time,
                        "edge_count_a_star": a_star_edge_count, "edge_count_dijkstras": dijkstras_edge_count, "edge_count_bellman_ford": bellman_ford_edge_count, "node_count_a_star": a_star_node_count, "node_count_dijkstras": dijkstras_node_count, "node_count_bellman_ford": bellman_ford_node_count})

    # error handling
    except Exception as e:
        app.logger.error(f"Error in /shortest_path: {e}")
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
