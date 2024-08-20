def bfs(graph, start_node):
    # Create a queue for BFS
    queue = [start_node]
    # Set of visited nodes
    visited = set()
    # Mark the source node as visited
    visited.add(start_node)

    while queue:
        # Dequeue a vertex from queue
        current_node = queue.pop(0)
        print(current_node, end=' ')

        # Get all adjacent vertices of the dequeued vertex
        for neighbour in graph[current_node]:
            if neighbour not in visited:
                # Enqueue the neighbour and mark it as visited
                queue.append(neighbour)
                visited.add(neighbour)

# Define the graph as an adjacency list
graph = {
    '0': ['1', '2', '3'],
    '1': ['4', '5'],
    '2': ['6','7'],
    '3': ['7'],
    '4': [],
    '5': [],
    '6': [],
    '7': []
}

# Perform BFS starting from node 'A'
bfs(graph, '0')



def bfs(graph, start_node, goal_node):
    # Create a queue for BFS
    queue = [start_node]
    # Set of visited nodes
    visited = set()
    # Mark the source node as visited
    visited.add(start_node)

    while queue:
        # Dequeue a vertex from queue
        current_node = queue.pop(0)
        print(current_node, end=' ')

        # If the goal node is found, stop the search
        if current_node == goal_node:
            print("\nGoal node found:", current_node)
            return

        # Get all adjacent vertices of the dequeued vertex
        for child in graph[current_node]:
            if child not in visited:
                # Enqueue the neighbour and mark it as visited
                queue.append(child)
                visited.add(child)

    print("\nGoal node not found in the graph.")

# Define the graph as an adjacency list
graph1 = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': [],
    'D': ['G'],
    'E': [],
    'F': [],
    'G': []
}

# Perform BFS starting from node 'A' with goal node 'E'
bfs(graph1, 'A', 'E')


class PriorityQueue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def insert(self, element, priority):
        self.queue.append((priority, element))

    def extract_max(self):
        if self.is_empty():
            return None
        
        # Find the element with the highest priority
        max_priority_index = 0
        for i in range(1, len(self.queue)):
            if self.queue[i][0] > self.queue[max_priority_index][0]:
                max_priority_index = i
        
        # Extract the element with the highest priority
        max_priority_element = self.queue[max_priority_index][1]
        del self.queue[max_priority_index]
        return max_priority_element

    def peek_max(self):
        if self.is_empty():
            return None

        max_priority_index = 0
        for i in range(1, len(self.queue)):
            if self.queue[i][0] > self.queue[max_priority_index][0]:
                max_priority_index = i

        return self.queue[max_priority_index][1]

# Example Usage
priority_queue = PriorityQueue()
priority_queue.insert("Task A", 2)
priority_queue.insert("Task B", 1)
priority_queue.insert("Task C", 3)

print("Element with highest priority:", priority_queue.peek_max())  # Should print "Task C"

while not priority_queue.is_empty():
    print(priority_queue.extract_max(), end=' ')  # Should print elements in order of priority: "Task C Task A Task B"


