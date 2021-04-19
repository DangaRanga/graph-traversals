"""Defines common graphing algorithms."""
import heapq
import enum
from collections import defaultdict


def lexico_dfs(visited, graph, node, latest=False):
    """Lexiographic Depth first search algorithm."""
    if node not in visited:
        visited.append(node)
        for neighbour in sorted(graph[node], reverse=latest):
            lexico_dfs(visited, graph, neighbour, latest=latest)


def remove_weights(graph):
    """Remove weights from a weighted graph.

    This is to peform BFS or dfs

    Args:
        <dict> graph: The graph datastructure

    Returns:
        None

    """
    for key, value in graph.items():

        neighbours = []
        for vertex in value:
            neighbours.append(vertex[0])
        graph[key] = neighbours


def lexico_bfs(graph, node, latest=False):
    """Lexiographic Breadth first search algorithm."""
    visited = [node]
    queue = [node]

    # Iterate whilst the queue isn't empty
    while queue:
        s = queue.pop(0)
        for neighbour in sorted(graph[s], reverse=latest):

            if len(neighbour) == 0:
                continue

            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
            else:
                continue
    return visited


def create_spanning_tree(graph, starting_vertex):
    """Create a minimal spanning tree and returns the traversal order.
    Using Prim's algorithm for a minimal spannning tree.

    From: https://bradfieldcs.com/algos/graphs/prims-spanning-tree-algorithm/

    Args:
        <dict> graph:
        <string> starting_vertex

    Returns:
        <list> The traversal order of the tree

    """
    # Initialize the minimal spanning tree
    mst = defaultdict(set)
    visited = [starting_vertex]
    edges = [
        (cost, starting_vertex, to)
        for to, cost in graph[starting_vertex].items()
    ]
    heapq.heapify(edges)

    while edges:
        cost, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.append(to)
            mst[frm].add(to)
            for to_next, cost in graph[to].items():
                if to_next not in visited:
                    heapq.heappush(edges, (cost, to, to_next))

    return list(visited)


def shortest_path(first_node, graph):
    """Dijkstra's algorithm for the shortest path in a graph.

    Args:
        first_node:
            <string> The first node in the graph
            <graph> An adjacency list representation of a graph, 
            where each edge is a dictionary with the nodes/vertexes

    Returns:
        <list> The traversal order of the graph

    """
    # To be refactored since dictionaries don't preserve order,
    # although this somehow preserves the order
    unvisited = {node: None for node in graph}  # using None as +inf
    visited = {}
    current = first_node
    current_distance = 0
    unvisited[current] = current_distance

    while True:
        for neighbour, distance in graph[current].items():
            if neighbour not in unvisited:
                continue
            new_distance = current_distance + distance
            if unvisited[neighbour] is None or unvisited[neighbour] > new_distance:
                unvisited[neighbour] = new_distance
        visited[current] = current_distance
        del unvisited[current]
        if not unvisited:
            break
        candidates = [node for node in unvisited.items() if node[1]]
        current, current_distance = sorted(candidates, key=lambda x: x[1])[0]

    return list(visited)


def tuple_edges_to_dict(graph):
    """Convert the tuple representation of the edges to a dictionary.

    Args:
        <dict> An adjacency list representation of the graph,
        with tuples as the edges

    Returns:
            <dict> An adjacency list representation of a graph
            where each edge is a dictionary with the nodes/vertexes

    """
    graph_copy = graph
    for key in graph_copy:
        graph_copy[key] = dict(graph_copy[key])
    return graph_copy


def parse_weighted_data(data_dict):
    """Update the graph dictionary with the evaluated data.

    Args:
        <dict> data_dict: A dictionary containing the data strings

    Returns:
        None

    """
    # Iterate over the dictionary
    for key, value in data_dict.items():
        data_dict[key] = data_dict[key].replace("\t", "")
        data_dict[key] = data_dict[key].replace(") (", "),(")

        # Parse the string if it isn't empty
        if data_dict[key] != "":
            print(data_dict[key])
            data_dict[key] = list(eval(data_dict[key]))
        else:
            # Welp this is probably dumb but it works for now
            data_dict[key] = ['Dead end']

        # Account for cases where there's only one element
        try:
            data_dict[key][0][1]
        except IndexError:
            data_dict[key] = [tuple((data_dict[key]))]


def parse_unweighted_data(data_dict):
    for key, value in data_dict.items():
        data_dict[key] = data_dict[key].replace("\t", "")
        data_dict[key] = data_dict[key].replace(" ", ",")
        data_dict[key] = data_dict[key].replace(" ", "")
        data_dict[key] = data_dict[key].split(",")


def update_data(data_dict, weighted=True):
    if weighted:
        parse_weighted_data(data_dict)
    else:
        parse_unweighted_data(data_dict)

# ---------------------  Current Instructions  ------------------------------ #

# Version 1.2 - With Prims and refactoring

# How to use:

# A function has been defined for each of the traversal methods,
# Copy the respective values from the tables and paste them in the graph
# dictionaries as strings as done below,
# the program handles parsing the data for you
# After which, run the respective function you need to acquire your result.

# Additionally, you will have to update the "latest" and "weighted" variables
# To account for when the graph is sorted by lexiographically "latest" ordering
# and if the graph is weighted or not

# Lastly, so you don't have to comment and uncomment out each traversal,
# I have added an options section to specify the traversal you would like to
# perform. After adding prims I hope to simply make this a commandline prompt
# To lessen the time even further.

# ---------------------  Paste Graph Values Here ---------------------------- #


# A F D E H B G C
# NB) If a node is not specified in the graph, comment it out.
# Especially for Prims and Dijkstra graphs, as it breaks the script
#  (I'll fix it in the future)

graph = {
    'A': "('C', 6) ('G', 6) ('H', 10)",
    'B': "('D', 15) ('F', 2) ('G', 19) ('H', 13)",
    'C': "('A', 6) ('D', 19) ('F', 2)",
    'D': "('B', 15) ('C', 19) ('E', 17) ('F', 16) ('G', 14)",
    'E': "('D', 17) ('F', 16) ('G', 15) ('H', 4)",
    'F': "('B', 2) ('C', 2) ('D', 16) ('E', 16) ('H', 17)",
    'G': "('A', 6) ('B', 19) ('D', 14) ('E', 15)",
    'H': "('A', 10) ('B', 13) ('E', 4) ('F', 17)"
}


class TraversalModes(enum.Enum):
    """Defines the traversal modes."""

    breadth_first = 'bfs'
    depth_first = 'dfs'
    dijkstra = 'dijkstra'
    prims = 'prims'


# Initializing parameters for methods
mode = TraversalModes('dijkstra')
starting_node = 'A'
weighted = True
latest = False

# Parses the data from the graph string
update_data(graph, weighted=weighted)

# Remove weighted for BFS and DFS
weighted_types = [TraversalModes.prims, TraversalModes.dijkstra]

if weighted and (mode not in weighted_types):
    remove_weights(graph)

# ---------------------  Function calls for BFS ----------------------------- #
if mode == TraversalModes.breadth_first:

    # Run Breadth first search
    bfs_visited_nodes = lexico_bfs(graph, starting_node, latest=latest)

    print(f'BFS visited nodes are: {bfs_visited_nodes}')

# ---------------------  Function calls for DFS ----------------------------- #
elif mode == TraversalModes.depth_first:

    # Run recursive depth first search
    visited_nodes = []
    lexico_dfs(visited_nodes, graph, starting_node, latest=latest)
    print(f'DFS visited are: {visited_nodes}')

# ---------------------  Function Call for Dijkstra's  ---------------------- #
elif mode == TraversalModes.dijkstra:

    # Create the graph to work with Dijkstra's
    newGraph = tuple_edges_to_dict(graph)

    # Run Dijkstra's algorithm to get the traversal order
    traversal_order = shortest_path(starting_node, newGraph)

    print(f'Dijkstra Traversal order: {traversal_order}')

# ---------------------  Function Call for Prim's  -------------------------- #
else:

    new_graph = tuple_edges_to_dict(graph)

    traversal_order = create_spanning_tree(new_graph, starting_node)
    print(f'Prims Traversal Order {traversal_order}')
