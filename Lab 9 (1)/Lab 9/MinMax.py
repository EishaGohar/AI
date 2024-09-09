graph = {
    'A': {'B', 'C'},
    'B': {'D', 'E'},
    'C': {'F', 'G'},
    'D': {'H', 'I'},
    'E': {'J', 'K'},
    'F': {'L', 'M'},
    'G': {'N', 'O'},
    'H': {},  # Terminal node with value -1
    'I': {},  # Terminal node with value 4
    'J': {},  # Terminal node with value 2
    'K': {},  # Terminal node with value 6
    'L': {},  # Terminal node with value -3
    'M': {},  # Terminal node with value -5
    'N': {},  # Terminal node with value 0
    'O': {}   # Terminal node with value 7
}

terminal_values = {
    'H': -1,
    'I': 4,
    'J': 2,
    'K': 6,
    'L': -3,
    'M': -5,
    'N': 0,
    'O': 7
}
def minimax(node, graph, max_func):
    if not graph[node]:  # Terminal condition (leaf node)
        return terminal_values[node]  # Return the terminal value
    
    if max_func:
        max_value = float('-inf')
        for child in graph[node]:
            value = minimax(child, graph, False)
            max_value = max(max_value, value)
        return max_value
    else:
        min_value = float('inf')
        for child in graph[node]:
            value = minimax(child, graph, True)
            min_value = min(min_value, value)
        return min_value    

# Run Minimax Algorithm
result = minimax('A', graph, True)
print("The optimal value is:", result)
