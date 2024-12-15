import time
import matplotlib.pyplot as plt
import numpy as np
from tspGA import genetic_algorithm as ga_algorithm  
from tspPSO import pso as pso_algorithm  

# Parameters
generations = 500
num_runs = 40  # Number of runs to calculate averages

def compare_algorithms():
    ga_times = []
    pso_times = []
    ga_best_distances = []  # Store the best distances found by GA
    pso_best_distances = []  # Store the best distances found by PSO
    ga_convergence = []
    pso_convergence = []

    for run in range(num_runs):
        print(f"Run {run + 1}/{num_runs}")

        # Run Genetic Algorithm
        start_time_ga = time.time()
        ga_best_individual, ga_best_distance, ga_convergence_data = ga_algorithm()
        end_time_ga = time.time()
        ga_times.append(end_time_ga - start_time_ga)
        ga_best_distances.append(ga_best_distance)
        ga_convergence.append(ga_convergence_data)

        # Run Particle Swarm Optimization
        start_time_pso = time.time()
        pso_best_individual, pso_best_distance, pso_convergence_data = pso_algorithm()
        end_time_pso = time.time()
        pso_times.append(end_time_pso - start_time_pso)
        pso_best_distances.append(pso_best_distance)
        pso_convergence.append(pso_convergence_data)

        print(f"GA Best Distance: {ga_best_distance}, PSO Best Distance: {pso_best_distance}")

    return ga_times, pso_times, ga_best_distances, pso_best_distances, ga_convergence, pso_convergence


def print_best_solutions(ga_best_distances, pso_best_distances):
    # Print best solution found for each run
    for run in range(len(ga_best_distances)):
        print(f"Run {run + 1}: GA Best Distance: {ga_best_distances[run]}, PSO Best Distance: {pso_best_distances[run]}")

    # Print the overall best solution from all runs
    best_ga_distance = min(ga_best_distances)
    best_pso_distance = min(pso_best_distances)
    
    print(f"\nOverall Best GA Distance: {best_ga_distance}")
    print(f"Overall Best PSO Distance: {best_pso_distance}")


def plot_comparison(ga_times, pso_times, ga_convergence, pso_convergence):
    # Plot execution time comparison
    plt.figure(figsize=(10, 6))
    plt.boxplot([ga_times, pso_times], labels=["GA", "PSO"], patch_artist=True)
    plt.title("Execution Time Comparison")
    plt.ylabel("Execution Time (seconds)")
    plt.grid(True)
    plt.show()

    # Plot convergence comparison
    ga_convergence = np.array(ga_convergence)  # Shape: (num_runs, generations)
    pso_convergence = np.array(pso_convergence)

    avg_ga_convergence = np.mean(ga_convergence, axis=0)
    avg_pso_convergence = np.mean(pso_convergence, axis=0)

    plt.figure(figsize=(10, 6))
    plt.plot(avg_ga_convergence, label="GA Convergence", color="blue")
    plt.plot(avg_pso_convergence, label="PSO Convergence", color="red")
    plt.title("Convergence Behavior Comparison")
    plt.xlabel("Generations")
    plt.ylabel("Fitness (Best Distance)")
    plt.legend()
    plt.grid(True)
    plt.show()


# Main execution
if __name__ == "__main__":
    print("Running comparisons...")
    ga_times, pso_times, ga_best_distances, pso_best_distances, ga_convergence, pso_convergence = compare_algorithms()
    print(f"\nAverage GA Time: {np.mean(ga_times):.4f} seconds")
    print(f"Average PSO Time: {np.mean(pso_times):.4f} seconds")
    
    # Print the best solutions found during the runs
    print_best_solutions(ga_best_distances, pso_best_distances)
    
    # Plot the comparisons
    plot_comparison(ga_times, pso_times, ga_convergence, pso_convergence)
