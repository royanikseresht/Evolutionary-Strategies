import numpy as np

def objective_function(x):
    return sum(x**2) # this is an example

def evolutionary_strategies(objective_function, num_generations, population_size, num_parameters, mutation_scale):
    population = np.random.rand(population_size, num_parameters)

    for generation in range(num_generations):
        fitness_values = [objective_function(individual) for individual in population]

        parents = population[np.argsort(fitness_values)[:population_size // 2]]

        offspring = parents + mutation_scale * np.random.randn(population_size // 2, num_parameters)

        population = np.vstack([parents, offspring])

    best_individual = population[np.argmin(fitness_values)]
    return best_individual

# Example usage
best_solution = evolutionary_strategies(objective_function, num_generations=100, population_size=50, num_parameters=5, mutation_scale=0.1)
print("Best solution found:", best_solution)
print("Objective function value:", objective_function(best_solution))