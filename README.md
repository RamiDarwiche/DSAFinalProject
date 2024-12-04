# DSAFinalProject
all the homies gon make it

Team Name: COP3530 Connoisseurs

Team Members: Rami Darwiche, Alexis Simpson, Sammy Li

Project Title: Comparison of GPS Path-finding Algorithms

Problem: What path-finding algorithms are most efficient for finding the shortest path
between two points on a real-world map?

Motivation: Figuring out the fastest path finding algorithm can help with improving
transportation efficiency (travel time and costs), and improving user experience.
- Also provides us with practical experience for getting familiar with path finding
algorithms.

Features and How To Use:
Our program displays a map of Gainesville, FL. Users can click anywhere on the map as their starting point and then click anywhere a second time to indicate their ending point. The map will then display the shortest path from the starting point to the ending point along the road network. A box on the side of the map will display details on the three shortest path algorithms we implemented. For each one, it will show the time in seconds that it took the algorithm to find the shortest path, the number of roads that the algorithm analyzed, and the number of intersections it analyzed. All of the shortest path algorithms will generate the same shortest path, just with different completion times and analysis methods.
JS 
Users can click the boxes on the bottom right of the screen to decide what information is viewable to them on the map. This includes removable route markers, algorithm comparison information, and general instructions for working the application.

Data: https://www.openstreetmap.org/#map=5/39.96/-97.82,
https://developers.google.com/maps

Tools: Python, Flask for backend implementation, Javascript, CSS, and HTML for building map frontend. Map provided by Leaflet JS API. OSMnx Python library used work with data obtained from OpenStreetMap.

Visuals:

![image](https://github.com/user-attachments/assets/a76a1ce9-711c-47b9-8beb-e1cf230ce087)

Strategy: We may want to implement shortest-path algorithms like A* search algorithm
and Dijkstra’s algorithm. We would represent the geographical data in a tree data
structure and then use our chosen algorithms to find the shortest paths between nodes
in this tree

Distribution of Responsibility and roles: Together we will build a tree to house the data.
Individually, we will each research and implement a different shortest-path algorithm.
After our individual implementations, we will rejoin to build the backend for a website in
Python using the Flask framework (Mostly Alexis and Sammy). The frontend will be built
last using React and Typescript (Mostly Rami).

References
- Shortest Path Algorithm Tutorial with Problems - GeeksforGeeks
- https://iaeme.com/MasterAdmin/Journal_uploads/IJMET/VOLUME_9_ISSUE_2/IJMET_09_02_078.pdf
- https://springerplus.springeropen.com/articles/10.1186/2193-1801-2-291
- https://osmnx.readthedocs.io/en/stable/user-reference.html
- https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.shortest_paths.astar.astar_path.html
- https://networkx.org/documentation/stable/reference/classes/generated/networkx.MultiDiGraph.nodes.html#networkx.MultiDiGraph.nodes
- https://networkx.org/documentation/stable/reference/classes/generated/networkx.MultiDiGraph.nodes.html#networkx.MultiDiGraph.nodes
