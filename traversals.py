import heapq
from collections import defaultdict

graph = {'A': [('E', 5), ('G', 7)], 'B': [('D', 10), ('F', 16)], 'C': [('B', 4), ('F', 9), ('H', 2)], 'D': [('A', 8), ('F', 4)], 'E': [('C', 16), ('H', 10)], 'F': [
    ('B', 14), ('G', 10), ('H', 6)], 'G': [('A', 3), ('B', 14), ('D', 8), ('E', 2), ('F', 13), ('H', 9)], 'H': [('B', 14), ('C', 12), ('E', 9)]}

nodes = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
distances = {
    'B': {'A': 5, 'D': 12, 'G': 2},
    'A': {'B': 5, 'D': 3, 'E': 12, 'F': 5},
    'D': {'B': 1, 'G': 1, 'E': 1, 'A': 3},
    'G': {'B': 2, 'D': 12, 'C': 2},
    'C': {'G': 2, 'E': 1, 'F': 16},
    'E': {'A': 12, 'D': 12, 'C': 1, 'F': 2},
    'F': {'A': 5, 'E': 2, 'C': 16}}


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


newGraph = tuple_edges_to_dict(graph)
print(shortest_path('A', newGraph))
