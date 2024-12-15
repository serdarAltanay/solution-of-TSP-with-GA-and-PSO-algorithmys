import random
import time

# my distances in distinct distances file to test my program with different size of city numbers you can add or remove # s to change cities matrix:

# from distances import distances_6 as distances
from distances import distances_10 as distances
# from distances import distances_15 as distances
# from distances import distances_20 as distances


# Parameters
num_cities = len(distances)
population_size = 12   
generations = 500
mutation_rate = 0.2
crossover_rate = 0.8   # Probability of performing crossover
tournament_size = 3    # Tournament selection size

# Fitness function: Calculate the total distance of a tour
def calculate_fitness(individual):
    total_distance = 0
    for i in range(len(individual) - 1):
        total_distance += distances[individual[i]][individual[i + 1]]  # Add distance between two cities
    total_distance += distances[individual[-1]][individual[0]]  # Add distance to return to the starting city
    return total_distance

# ınitialize population with random individuals
def initialize_population(size, num_cities):
    population = []
    for _ in range(size):
        individual = list(range(1, num_cities))  # all individuals start with city 0 and end with city 0
        random.shuffle(individual)
        individual = [0] + individual + [0]  # Add city 0 at start and end
        population.append(individual)
    return population

# Tournament Selection
def tournament_selection(population, fitnesses, tournament_size):
    selected = random.sample(range(len(population)), tournament_size)  # Select individuals randomly
    best_fitness = float('inf')
    for individual in selected:
        if fitnesses[individual] < best_fitness:
            best_fitness = fitnesses[individual]
            best_individual = individual
    return population[best_individual]

def crossover(parent1, parent2):
    # Step 1: Calculate the segment sizes
    # Calculate the size of each segment for 3 equal parts(two point creossover)
    segment_length = (num_cities - 2) // 3  # Exclude city 0
    start1, end1 = 1, segment_length
    start2, end2 = end1 + 1, 2 * segment_length
    start3, end3 = end2 + 1, num_cities - 2
    
    # Step 2: Create the child tour with -1 placeholders
    child = [-1] * num_cities  # Initialize with -1, representing unfilled positions
    child[0] = child[-1] = 0   # Fixed cities at the start and end
    
    # Step 3: Copy the segments from parent1 to the child
    child[start1:end1 + 1] = parent1[start1:end1 + 1]
    child[start2:end2 + 1] = parent1[start2:end2 + 1]
    child[start3:end3 + 1] = parent1[start3:end3 + 1]
    
    # Step 4: Fill the remaining positions in the child with genes from parent2
    pointer = 1  # Start filling positions from city 1 onwards
    for gene in parent2:
        # Skip cities that are already in the child
        if gene not in child:
            # Move the pointer to the next available position in the child
            while child[pointer] != -1 and pointer < num_cities - 1:
                pointer += 1
            # Place the gene from parent2 into the next empty position
            child[pointer] = gene
    
    return child



# Mutation: Swap two cities
def mutate(individual):
    if random.random() < mutation_rate:
        i, j = random.sample(range(1, len(individual) - 1), 2)  # Exclude 0
        individual[i], individual[j] = individual[j], individual[i] #swaping

def genetic_algorithm():
    population = initialize_population(population_size, num_cities)
    best_individual = None
    best_distance = float('inf')
    
    convergence_data = []  # Store best distances per generation to visualize convergancy

    for generation in range(generations):
        # Calculate fitnesses
        fitnesses = [calculate_fitness(individual) for individual in population]

        # Update the best solution
        current_best_idx = fitnesses.index(min(fitnesses))
        if fitnesses[current_best_idx] < best_distance:
            best_distance = fitnesses[current_best_idx]
            best_individual = population[current_best_idx]

        # Append the best distance of this generation
        convergence_data.append(best_distance)

        # Create the next generation
        new_population = []
        for _ in range(population_size // 2):  # Generate pairs of offspring
            parent1 = tournament_selection(population, fitnesses, tournament_size)
            parent2 = tournament_selection(population, fitnesses, tournament_size)

            if random.random() < crossover_rate:
                child1 = crossover(parent1, parent2)
                child2 = crossover(parent2, parent1)
            else:
                child1, child2 = parent1[:], parent2[:]

            mutate(child1)
            mutate(child2)

            new_population.extend([child1, child2])

        population = new_population

    return best_individual, best_distance, convergence_data

    

start_time = time.time()
best_individual_ga, best_distance_ga,convergence_data = genetic_algorithm()
end_time = time.time()
ga_time = end_time - start_time
print("Best Tour:", [chr(65 + city) for city in best_individual_ga])
print("Best Distance:", best_distance_ga)
print(f"Execution Time: {end_time - start_time:.4f} seconds")


# Pseduecode of GA:
# Initialize population with random individuals
# Evaluate the fitness of each individual in the population
# While termination condition not met
#   Select parents from the population based on their fitness
#   Apply crossover to selected parents to create offspring
#   Apply mutation to offspring for variation
#   Evaluate the fitness of the offspring
#   Select individuals for the next generation (elitism can be applied)
# Return the best solution found



# Exmaple individual:
# cities numbered with ist own IDs
# individual = [0, 4, 3, 1, 5, 2, 0]


# Example population:
# population = [
#     [0, 4, 3, 1, 5, 2, 0],
#     [0, 2, 3, 5, 4, 1, 0],
#     [0, 1, 4, 5, 3, 2, 0],
#     # ... up to `population_size`
# ]


# The time complexity of this genetic algorithm is:

# O(generations×population_size×number_of_cities)