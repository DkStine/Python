'''
from queue import PriorityQueue

def reconstruct_path(came_from, start, goal):
    current = goal
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path

class Graph:
    def __init__(self, graph_dict=None):
        if graph_dict is None:
            graph_dict = {}
        self.graph_dict = graph_dict

    def neighbors(self, node):
        return self.graph_dict.get(node, {}).keys()

    def cost(self, from_node, to_node):
        return self.graph_dict.get(from_node, {}).get(to_node, float('inf'))

def a_star_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}

    while not frontier.empty():
        current = frontier.get()[1]

        if current == goal:
            break

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost  # No heuristic
                frontier.put((priority, next))
                came_from[next] = current

    return reconstruct_path(came_from, start, goal), cost_so_far

graph_data = {
    'B': {'D': 5},
    'A': {'B': 2,'C': 1},
    'C': {'D': 3,'G': 4},
    'D': {'G': 2},
    'S': {'G': 10,'A': 1},
    'G': {}
}
graph = Graph(graph_data)
start = 'S'
goal = 'G'
path, cost = a_star_search(graph, start, goal)
print("Path:", path)
print("Cost:", cost)
'''

from queue import PriorityQueue

def uniform_cost_search(graph, start, goal):
    # Create a priority queue to store (cost, node, path) tuples
    q = PriorityQueue()
    q.put((0, start, []))  # Start with the initial node with 0 cost and empty path

    visited = set()  # To keep track of visited nodes

    while not q.empty():
        cost, node, path = q.get()  # Get the node with the lowest cost

        # If the node is the goal, return the path and cost
        if node == goal:
            return path + [node], cost

        # If the node has already been visited, skip it
        if node in visited:
            continue

        # Mark the node as visited
        visited.add(node)

        # Expand the current node and add its neighbors to the queue
        for neighbor, neighbor_cost in graph.get(node, []):
            if neighbor not in visited:
                q.put((cost + neighbor_cost, neighbor, path + [node]))

    return None, float('inf')  # If no path is found

# Example usage
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('D', 2), ('E', 5)],
    'C': [('A', 4), ('F', 3)],
    'D': [('B', 2), ('E', 1)],
    'E': [('B', 5), ('D', 1), ('F', 2)],
    'F': [('C', 3), ('E', 2)],
}

start = 'A'
goal = 'F'
path, cost = uniform_cost_search(graph, start, goal)
print(f"Path: {path}, Cost: {cost}")