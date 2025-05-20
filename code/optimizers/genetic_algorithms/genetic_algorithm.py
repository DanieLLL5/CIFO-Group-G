import random
import numpy as np

class GeneticAlgorithm:
    def __init__(self, helper, pop_size=100, num_gen=50, p_xo=0.8, p_m=0.05, selection_method="battle",
                 elitism=False, n_elite=10, n_battles=5, p_pity=0.0001,
                 swap=True, table_flip=True, relationship_augmenter=True,
                 selection_func=None, crossover_func=None, mutation_func=None):
        """
        Initialize the genetic algorithm.

        :param helper: helper object/class with fitness and generate_solution methods
        :param pop_size: Population size
        :param num_gen: Number of generations
        :param p_xo: Probability of crossover
        :param p_m: Probability of mutation
        :param selection_method: Selection algorithm name
        :param elitism: Use elitism or not
        :param n_elite: Number of elite individuals
        :param n_battles: Number of battles in battle selection
        :param p_pity: Probability of pity selection
        :param swap: Enable swap mutation
        :param table_flip: Enable table flip mutation
        :param relationship_augmenter: Enable relationship augmenter mutation
        :param selection_func: Function to handle selection
        :param crossover_func: Function to handle crossover
        :param mutation_func: Function to handle mutation
        """

        self.helper = helper
        self.pop_size = pop_size
        self.num_gen = num_gen
        self.p_xo = p_xo
        self.p_m = p_m
        self.selection_method = selection_method
        self.elitism = elitism
        self.n_elite = n_elite
        self.n_battles = n_battles
        self.p_pity = p_pity
        self.swap = swap
        self.table_flip = table_flip
        self.relationship_augmenter = relationship_augmenter
        
        # Dependency injections or default implementations
        self.selection_func = selection_func
        self.crossover_func = crossover_func
        self.mutation_func = mutation_func

    def run(self, return_fitness_curve=False):
        best_fitness = float("-inf")
        best_solution = None
        fitness_curve = []

        # Initialize population
        population = [self.helper.generate_solution() for _ in range(self.pop_size)]

        for gen in range(self.num_gen):
            # Evaluate fitness of current population
            fitnesses = [self.helper.fitness(ind) for ind in population]

            # Save best of this generation
            max_fitness = max(fitnesses)
            max_index = fitnesses.index(max_fitness)

            if max_fitness > best_fitness:
                best_fitness = max_fitness
                best_solution = population[max_index]

            if return_fitness_curve:
                fitness_curve.append(max_fitness)

            # Apply selection
            selected = self.selection_func(population, fitnesses, method=self.selection_method, **self.selection_args)

            # Apply crossover
            offspring = []
            while len(offspring) < self.pop_size:
                parent1, parent2 = random.sample(selected, 2)
                if random.random() < self.p_xo:
                    child1, child2 = self.crossover_func(parent1, parent2)
                    offspring.extend([child1, child2])
                else:
                    offspring.extend([copy.deepcopy(parent1), copy.deepcopy(parent2)])

            offspring = offspring[:self.pop_size]  # Trim extra if needed

            # Apply mutation
            for i in range(len(offspring)):
                if random.random() < self.p_m:
                    offspring[i] = self.mutation_func(
                        offspring[i],
                        swap=self.swap,
                        table_flip=self.table_flip,
                        relationship_augmenter=self.relationship_augmenter
                    )

            # Apply elitism if enabled
            if self.elitism:
                elite_indices = sorted(range(len(fitnesses)), key=lambda i: fitnesses[i], reverse=True)[:self.n_elite]
                elites = [population[i] for i in elite_indices]
                offspring[:self.n_elite] = elites

            # Replace old population
            population = offspring

        return (best_fitness, fitness_curve) if return_fitness_curve else (best_fitness, best_solution)
