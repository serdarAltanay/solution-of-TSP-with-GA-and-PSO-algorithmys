import random
import time

# my distances in distinct distances file to test my program with different size of city numbers you can add or remove # s to change cities matrix:
# from distances import distances_6 as distances
from distances import distances_10 as distances
# from distances import distances_15 as distances
# from distances import distances_20 as distances

# Parameters
num_cities = len(distances)
swarm_size = 30  # Number of particles
generations = 500
w = 0.5  # Inertia weight
c1 = 1.5  # Cognitive coefficient
c2 = 1.5  # Social coefficient

# Fitness function
def calculate_fitness(individual):
    total_distance = 0
    for i in range(len(individual) - 1):
        total_distance += distances[individual[i]][individual[i + 1]]
    total_distance += distances[individual[-1]][individual[0]]
    return total_distance

# Initialize swarm with random positions and velocities
def initialize_swarm():
    swarm = []
    velocities = []
    for _ in range(swarm_size):
        # Generate a random tour (position) with no duplicates
        position = list(range(1, num_cities))
        random.shuffle(position)
        position = [0] + position + [0]  # City 0 is fixed at the start and end
        velocity = [random.randint(-1, 1) for _ in range(num_cities)]  # Random velocity
        swarm.append(position)
        velocities.append(velocity)
    return swarm, velocities

# Update velocity and position for each particle
def update_velocity_position(swarm, velocities, pBest, gBest):
    new_swarm = []
    new_velocities = []
    for i in range(swarm_size):
        # Update velocity using Eq 1
        velocity = velocities[i]
        position = swarm[i]
        
        for j in range(1, num_cities - 1):  # Exclude fixed city 0
            r1 = random.random()
            r2 = random.random()
            velocity[j] = (w * velocity[j] + c1 * r1 * (pBest[i][j] - position[j]) +
                           c2 * r2 * (gBest[j] - position[j]))

        # Update position using velocity (perform a valid swap based on velocity)
        new_position = position[:]
        for j in range(1, num_cities - 1):
            swap_idx = int(velocity[j] % (num_cities - 1)) + 1  # Get the index to swap with
            new_position[j], new_position[swap_idx] = new_position[swap_idx], new_position[j]

        # Ensure no duplicates or missing cities
        new_position = fix_invalid_tour(new_position)

        new_swarm.append(new_position)
        new_velocities.append(velocity)
    return new_swarm, new_velocities

# Fix invalid tours (ensure no duplicates in the tour)
def fix_invalid_tour(position):
    visited = set()
    for i in range(1, len(position) - 1):
        while position[i] in visited:
            # If a duplicate city is found, swap it with a random city
            swap_idx = random.randint(1, len(position) - 2)
            position[i], position[swap_idx] = position[swap_idx], position[i]
        visited.add(position[i])
    return position

def pso():
    convergence_data = []  # Store best distances per generation to visualize convergancy
    swarm, velocities = initialize_swarm()

    pBest = swarm[:]
    pBest_fitness = [calculate_fitness(ind) for ind in pBest]
    gBest = pBest[pBest_fitness.index(min(pBest_fitness))]
    gBest_fitness = min(pBest_fitness)

    for generation in range(generations):
        fitnesses = [calculate_fitness(ind) for ind in swarm]

        # Update pBest and gBest
        for i in range(swarm_size):
            if fitnesses[i] < pBest_fitness[i]:
                pBest[i] = swarm[i]
                pBest_fitness[i] = fitnesses[i]

        best_in_swarm = min(fitnesses)
        if best_in_swarm < gBest_fitness:
            gBest = swarm[fitnesses.index(best_in_swarm)]
            gBest_fitness = best_in_swarm

        # Append the best distance of this generation
        convergence_data.append(gBest_fitness)

        swarm, velocities = update_velocity_position(swarm, velocities, pBest, gBest)

    return gBest, gBest_fitness, convergence_data


# Run PSO
start_time = time.time()
best_individual_pso, best_distance_pso,convergence_data = pso()
end_time = time.time()
pso_time = end_time - start_time


print("\nParticle Swarm Optimization:")
print("Best Tour:", [chr(65 + city) for city in best_individual_pso])
print("Best Distance:", best_distance_pso)
print(f"Execution Time: {end_time - start_time:.4f} seconds")


# Pseduecode of PSO: 
# Initialize swarm with random positions and velocities
# For each particle, calculate its fitness and set  pBest = current position 
# Set  gBest as the position with the best fitness in the swarm 
# Repeat until termination condition:
#   For each particle:
#       Update velocity using  eq 1 
#       Update position using  eq 2 
#       Evaluate the fitness of the new position
#       If the new fitness is better than  pBest 
#           Update  pBest = new position 
#       If  pBest is better than gBest 
#           Update  gBest = pBest 
# Return gBest as the best solution found


# Example swarm (with random initial positions):
# swarm = [
#     [0, 2, 5, 3, 4, 1, 0],  # Particle 1
#     [0, 4, 3, 1, 2, 5, 0],  # Particle 2
#     [0, 5, 1, 4, 3, 2, 0],  # Particle 3
#     ...
# ]

# Example velocities (random initial velocities):
# velocities = [
#     [0, 1, -1, 0, 1, -1, 0],  # Particle 1 velocity
#     [-1, 1, 0, 1, -1, 0, 0],  # Particle 2 velocity
#     [0, -1, 1, -1, 1, 0, 0],  # Particle 3 velocity
#     ...
# ]


# time complexity of this algorithm is:
#
#     O(generations×swarm_size×number_of_cities)
