graph = {
    'A': ['B','F','D','E'],
    'B': ['K', 'J'],
    'C': [],
    'D': ['G'],
    'E': ['C','H','I'],
    'F': [],
    'G': [],
    'H': [],
    'I': ['L'],
    'J': [],
    'K': ['N','M'],
    'L':[],
    'M':[],
    'N':[]

}

# Depth First Search implementation using a stack
def dfs(graph, start, goal):
    visited = set()
    
    # stack = [start]
    stack = []
    stack.append(start)
    

    while stack:
        node = stack.pop()

        if node == goal:
            print(f"Goal node {goal} found!")
            return True

        if node not in visited:
            print(f"Visiting node: {node}")
            visited.add(node)
            
            # stack.extend(reversed(graph[node]))
            for child in reversed(graph[node]):
                if child not in visited:
                    stack.append(child)
    
    print(f"Goal node {goal} not found in the graph.")
    return False

# Call the DFS function from node A to G
dfs(graph, 'A', 'G')