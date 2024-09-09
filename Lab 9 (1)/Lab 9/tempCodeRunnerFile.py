graph = {
    'A': {'B', 'C'},
    'B': {'D', 'E'},
    'C': {'F', 'G'},
    'D': {'3', '5'},
    'E': {'6', '9'},
    'F': {'1', '2'},
    'G': {'0', '-1'},
    '3': {},
    '5': {},
    '6': {},
    '9': {},
    '1': {},
    '2': {},
    '0': {},
    '-1': {}
}
def alpha_beta_pruning(node,graph,max_func,alpha,beta):
    if  not  graph[node]:
        return int(node)
    if max_func:
        max_value = float('-inf')
        for child in graph[node]:
            value = alpha_beta_pruning(child,graph,False,alpha,beta)
            max_value=max(max_value,value)
            alpha = max(alpha, value)
            if beta <= alpha:
                break
        return max_value
    else:
        min_value = float('inf')
        for child in graph[node]:
            value = alpha_beta_pruning(child,graph,True,alpha,beta)
            min_value=min(min_value,value)
            beta=min(value,beta)
            if beta <=alpha:
                break
        return min_value    




alpha = float('-inf')
beta = float('inf')
result = alpha_beta_pruning('A', graph, True, alpha, beta)
print("The optimal value is:", result)
