import math
import random

# Define the function to minimize
def f(x, y):
    return x**2 + y**2

# Simulated Annealing algorithm
def simulated_annealing(start_x, start_y, step_size=0.1, initial_temp=200, cooling_rate=2, max_iterations=1000):
    current_solution_x = start_x
    current_solution_y = start_y
    current_value = f(current_solution_x, current_solution_y)
    
    temperature = initial_temp

    for i in range(max_iterations):
        if temperature <= 0:
            break
        
        # Generate a new solution by moving to a random neighboring point
        new_solution_x = current_solution_x + random.uniform(-step_size, step_size)
        new_solution_y = current_solution_y + random.uniform(-step_size, step_size)
        
        # Evaluate the function at the new point
        new_value = f(new_solution_x, new_solution_y)
        
        # Calculate the change in value
        delta_value = new_value - current_value
        
        # Decide whether to move to the new point
        if delta_value < 0 or random.uniform(0, 1) < math.exp(-delta_value / temperature):
            # Move to the new solution
            current_solution_x = new_solution_x
            current_solution_y = new_solution_y
            current_value = new_value
        
        # Cool down the temperature
        temperature = temperature/cooling_rate

    return current_solution_x, current_solution_y, current_value

# Define the search space boundaries
x_min, x_max = -10, 10
y_min, y_max = -10, 10

# Randomly initialize x and y within the search space
start_x = random.uniform(x_min, x_max)
start_y = random.uniform(y_min, y_max)

# Run the Simulated Annealing algorithm
solution_x, solution_y, value = simulated_annealing(start_x, start_y)

print(f"Starting point: ({start_x}, {start_y})")
print(f"Optimal solution: ({solution_x}, {solution_y})")
print(f"Function value at optimal solution: {value}")
