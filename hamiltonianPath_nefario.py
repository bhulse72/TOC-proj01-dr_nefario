#!/usr/bin/env python3

import collections
import sys
import time

# Type Aliases
Graph = dict[int, set[int]]

# Read Graph
def read_graph(stream) -> Graph:
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
            _, graph_type, num_vertices, num_edges = line.split(',')
            num_vertices = int(num_vertices)
            num_edges = int(num_edges)
            # You can process graph_type (e.g., 'u' for undirected, 'd' for directed) if needed

        else:
            # Handle vertex or edge lines
            parts = line.split(',')
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
                if graph_type == 'u':  # If undirected, add both directions
                    graph[destination_id].add(source_id)

    return graph, problem_number

# Find Hamiltonian Path
def find_hamiltonian_path(graph: Graph, vertex: int, visited: set[int], path_length: int) -> bool:
    if path_length == len(graph):
        return True

    for neighbor in sorted(graph[vertex]):
        if neighbor not in visited:
            visited.add(neighbor)
            if find_hamiltonian_path(graph, neighbor, visited, path_length + 1):
                return True
            visited.remove(neighbor)

    return False

def main(arguments=sys.stdin):
    '''
    while True: 
        try:
            Ni = int(arguments.readline().strip())
        except ValueError:
            break
'''
        # Start timing the reading of the graph
        start_time = time.time()
        graph, problem_number = read_graph(arguments)
        read_time = time.time() - start_time  # Calculate the time taken to read the graph

        # Start timing the Hamiltonian path search
        start_time = time.time()
        visited = {1}
        path_length = 1  # Start counting with the first vertex
        has_path = find_hamiltonian_path(graph, 1, visited, path_length)
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

