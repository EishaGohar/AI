def GBFS(start,end):
    distance=0
    queue=[]
    visited=set()
    queue.append((start,0)) #list of tuples including node and its weight like ('node',3)
    while queue:
        queue.sort(key=lambda x: x[1]) #sorting queue on basis of weight
        node,weight=queue.pop(0)
        distance+=weight
        
        if node not in visited:
            print(node,end=" --> ")
            visited.add(node)
        if node==end:
            print(f'\nDistance taken from {start} to {end} : {distance}')
            break
        for adjacent in graph[node]['Adjacents']:
            if adjacent not in visited:
                queue.append((adjacent,graph[node]['Adjacents'][adjacent]))
                
        
graph = {
        'Oradea': {'Adjacents': {'Zerind': 71, 'Sibiu': 151}},
        'Zerind': {'Adjacents': {'Oradea': 71, 'Arad': 75}},
        'Arad': {'Adjacents': {'Zerind': 75, 'Timisoara': 118, 'Sibiu': 140}},
        'Sibiu': {'Adjacents': {'Oradea': 151, 'Arad': 140, 'Fagaras': 99, 'Rimnicu Vilcea': 80}},
        'Timisoara': {'Adjacents': {'Arad': 118, 'Lugoj': 111}},
        'Lugoj': {'Adjacents': {'Timisoara': 111, 'Mehadia': 70}},
        'Mehadia': {'Adjacents': {'Lugoj': 70, 'Dobreta': 75}},
        'Dobreta': {'Adjacents': {'Mehadia': 75, 'Craiova': 120}},
        'Craiova': {'Adjacents': {'Dobreta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138}},
        'Rimnicu Vilcea': {'Adjacents': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97}},
        'Pitesti': {'Adjacents': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101}},
        'Fagaras': {'Adjacents': {'Sibiu': 99, 'Bucharest': 211}},
        'Bucharest': {'Adjacents': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85}},
        'Giurgiu': {'Adjacents': {'Bucharest': 90}},
        'Urziceni': {'Adjacents': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142}},
        'Hirsova': {'Adjacents': {'Urziceni': 98, 'Eforie': 86}},
        'Eforie': {'Adjacents': {'Hirsova': 86}},
        'Vaslui': {'Adjacents': {'Urziceni': 142, 'Iasi': 92}},
        'Iasi': {'Adjacents': {'Vaslui': 92, 'Neamt': 87}},
        'Neamt': {'Adjacents': {'Iasi': 87}},
    }
GBFS('Oradea','Sibiu')


