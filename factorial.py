import itertools

def calculate_route_distance(route, distance_matrix):
    """Calculates the total distance of a given Hamiltonian circuit."""
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distance_matrix[route[i]][route[i+1]]

    total_distance += distance_matrix[route[-1]][route[0]]
    return total_distance

def main():

    nodes = ['A', 'B', 'C', 'D', 'E', 'F']
    
   
    distance_matrix = {
        'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20, 'E': 25, 'F': 30},
        'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25, 'E': 15, 'F': 20},
        'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30, 'E': 10, 'F': 40},
        'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0, 'E': 5,  'F': 15},
        'E': {'A': 25, 'B': 15, 'C': 10, 'D': 5,  'E': 0, 'F': 50},
        'F': {'A': 30, 'B': 20, 'C': 40, 'D': 15, 'E': 50, 'F': 0}
    }

    start_node = 'A'
    other_nodes = [node for node in nodes if node != start_node]
    
    all_permutations = list(itertools.permutations(other_nodes))
    
    best_distance = float('inf')
    best_route = None
    
    print(f"=== BRUTE FORCE HAMILTONIAN CIRCUIT FINDER (6 NODES) ===")
    print(f"Total possible node ordering permutations (5!): {len(all_permutations)}\n")

    for perm in all_permutations:
        current_route = [start_node] + list(perm)
        current_distance = calculate_route_distance(current_route, distance_matrix)
        
        if current_distance < best_distance:
            best_distance = current_distance
            best_route = current_route

    full_path = " -> ".join(best_route) + f" -> {start_node}"
    print("-" * 55)
    print(f"FASTEST ROUTE FOUND : {full_path}")
    print(f"MINIMUM DISTANCE    : {best_distance} meters")
    print("-" * 55)

if __name__ == "__main__":
    main()