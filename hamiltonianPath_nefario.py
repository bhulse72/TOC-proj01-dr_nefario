#!/usr/bin/env python3

import collections
import sys
import time

# Type Aliases
Graph = dict[int, set[int]]

# Read Graph
def read_graph(stream) -> tuple[Graph, int]:
    graph: Graph = collections.defaultdict(set)
    problem_number = None

    for line in stream:
        line = line.strip()
        if not line:
            continue  # Skip empty lines

        if line.startswith('c'):
            # Handle comment lines
            comment_info = line[2:]  # Skip 'c,'
            problem_number = int(comment_info.split(',')[0])  # Extract problem number

        elif line.startswith('p'):
            # Handle problem line
            _, graph_type, num_vertices, num_edges = line.split(', ')
            num_vertices = int(num_vertices)
            num_edges = int(num_edges)

        else:
            # Handle vertex or edge lines
            parts = line.split(', ')
            class_name = parts[0]

            if class_name == 'v':
                # Vertex line
                vertex_id = int(parts[1])  # Assuming the second parameter is the vertex id
                graph[vertex_id]  # Initialize the vertex in the graph
            elif class_name == 'e':
                # Edge line
                source_id = int(parts[1])
                destination_id = int(parts[2])
                graph[source_id].add(destination_id)
                graph[destination_id].add(source_id)  # Undirected graph

    # Ensure all vertices are included in the graph
    for vertex in range(1, num_vertices + 1):
        graph.setdefault(vertex, set())

    return graph, problem_number

# Recursive function to find Hamiltonian Path
def find_hamiltonian_path(graph: Graph, path: list[int], visited: set[int]) -> bool:
    if len(path) == len(graph):  # All vertices are visited
        return True

    last_vertex = path[-1]

    for neighbor in graph[last_vertex]:
        if neighbor not in visited:
            # Mark the neighbor as visited
            visited.add(neighbor)
            path.append(neighbor)

            if find_hamiltonian_path(graph, path, visited):
                return True

            # Backtrack: Unmark the neighbor and remove from path
            visited.remove(neighbor)
            path.pop()

    return False

# Wrapper function to initiate the search
def has_hamiltonian_path(graph: Graph) -> bool:
    for start_vertex in graph.keys():
        path = [start_vertex]
        visited = {start_vertex}

        if find_hamiltonian_path(graph, path, visited):
            return True

    return False

def main(arguments=sys.stdin):
    # Start timing the reading of the graph
    start_time = time.time()
    graph, problem_number = read_graph(arguments)
    read_time = time.time() - start_time  # Calculate the time taken to read the graph

    # Start timing the Hamiltonian path search
    start_time = time.time()

    has_path = has_hamiltonian_path(graph)
    search_time = time.time() - start_time  # Calculate the time taken to find the path
    
    if has_path:
        print("Yes")
    else:
        print("No")
    
    # Print timing information
    print(f"Time to read graph: {read_time:.6f} seconds")
    print(f"Time to find Hamiltonian path: {search_time:.6f} seconds")

if __name__ == '__main__':
    main()
