import random

def f(x, y):
    return x**2 + y**2

def hill_climbing_2d(start_x, start_y, step_size=0.25, max_iterations=1000):
    current_solution_x = start_x
    current_solution_y = start_y
    current_value = f(current_solution_x, current_solution_y)
    
    for _ in range(max_iterations):
        neighbors = [
            (current_solution_x + step_size, current_solution_y),     
            (current_solution_x - step_size, current_solution_y),                 
            (current_solution_x, current_solution_y + step_size),               
            (current_solution_x, current_solution_y - step_size),                 
            (current_solution_x + step_size, current_solution_y + step_size),
            (current_solution_x - step_size, current_solution_y + step_size),
            (current_solution_x + step_size, current_solution_y - step_size),
            (current_solution_x - step_size, current_solution_y - step_size)
        ]
        best_neighbor = None
        best_value = current_value
        
        for (neighbor_x, neighbor_y) in neighbors:
            neighbor_value = f(neighbor_x, neighbor_y)
            if neighbor_value < best_value:
                best_value = neighbor_value
                best_neighbor = (neighbor_x, neighbor_y)
        
        if best_neighbor is None:
            break

        current_solution_x, current_solution_y = best_neighbor
        current_value = best_value

    return current_solution_x, current_solution_y, current_value

# start_x = random.uniform(-10, 10)
# start_y = random.uniform(-10, 10)
start_x = 4
start_y = 4
solution_x, solution_y, value = hill_climbing_2d(start_x, start_y)

print(f"Starting point: ({start_x}, {start_y})")
print(f"Optimal solution: ({solution_x}, {solution_y})")
print(f"Function value at optimal solution: {value}")
