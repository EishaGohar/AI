
def Astar(start_node, goal_node):
    
    # Estimated distances to the goal (heuristic)
    heuristic = {
        'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Dobreta': 242, 'Eforie': 161, 'Fagaras': 176,
        'Giurgiu': 77, 'Hirsova': 151, 'Iasi': 226, 'Lugoj': 244, 'Mehadia': 241, 'Neamt': 234,
        'Oradea': 380, 'Pitesti': 10, 'Rimnicu Vilcea': 193, 'Sibiu': 253, 'Timisoara': 329,
        'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374
    }

    # Map of cities and distances between them
    graph = {
        'Oradea': {'Zerind': 71, 'Sibiu': 151},
        'Zerind': {'Oradea': 71, 'Arad': 75},
        'Arad': {'Zerind': 75, 'Timisoara': 118, 'Sibiu': 140},
        'Sibiu': {'Oradea': 151, 'Arad': 140, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
        'Timisoara': {'Arad': 118, 'Lugoj': 111},
        'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
        'Mehadia': {'Lugoj': 70, 'Dobreta': 75},
        'Dobreta': {'Mehadia': 75, 'Craiova': 120},
        'Craiova': {'Dobreta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
        'Rimnicu Vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
        'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
        'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
        'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
        'Giurgiu': {'Bucharest': 90},
        'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
        'Hirsova': {'Urziceni': 98, 'Eforie': 86},
        'Eforie': {'Hirsova': 86},
        'Vaslui': {'Urziceni': 142, 'Iasi': 92},
        'Iasi': {'Vaslui': 92, 'Neamt': 87},
        'Neamt': {'Iasi': 87},
    }

    # This checks if the start or goal node is not in the map
    if start_node not in graph or goal_node not in graph:
        print("Invalid node")
        return
    
    # A list to keep track of nodes to explore
    queue = [(heuristic[start_node], start_node)]
    
    # Distances from the start node to each node
    g_n = {node: float('inf') for node in graph}
    g_n[start_node] = 0
    
    visited = set()

    while queue:
        # Get the node with the lowest cost
        queue.sort()
        current_cost, node = queue.pop(0)

        if node in visited:
            continue

        visited.add(node)
        print(f"Visiting {node}")

        # If we've reached the goal, print the distance and stop
        if node == goal_node:
            print(f"Reached {goal_node}, Total Distance: {g_n[goal_node]}")
            return

        # Check all connected nodes
        for adjacent, distance in graph[node].items():
            if adjacent not in visited:
                new_cost = g_n[node] + distance
                if new_cost < g_n[adjacent]:
                    g_n[adjacent] = new_cost
                    queue.append((new_cost + heuristic[adjacent], adjacent))

# Example usage
Astar('Oradea', 'Bucharest')
