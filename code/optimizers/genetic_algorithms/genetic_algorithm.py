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

    def run(self):
        #Generate a random initial population
        population = [self.helper.generate_solution() for _ in range(self.pop_size)]

        for i in range(self.num_gen):
            print(f"gen {i}")
            #Probablistically the best individuals pass the selection process
            selected_population = self.selection_func(
            population = self.selection_func(
                population,
                self.pop_size,
                self.helper,
                selection=self.selection_method,
                elitism=self.elitism,
                n_elite=self.n_elite,
                n_battles=self.n_battles,
                p_pity=self.p_pity
            )

            #Some will do crossover, some will mutate and others will stay as is for the next generation
            for i in range(self.pop_size // 2):

            new_population = []
            crossedover_indexes = []
            mutated_indexes = []

            #Crossover
            for i in range(0,self.pop_size-1,2):
                if random.random() < self.p_xo:
                    selected_population[i], selected_population[-i-1] = self.crossover_func(
                        selected_population[i], selected_population[-i-1])
                elif random.random() < self.p_m * 2:
                    if random.random() < 0.5:
                        selected_population[i] = self.mutation_func(
                            selected_population[i], self.helper, self.swap, self.table_flip, self.relationship_augmenter)
                    else:
                        selected_population[-i-1] = self.mutation_func(
                            selected_population[-i-1], self.helper, self.swap, self.table_flip, self.relationship_augmenter)
                    child1, child2 = self.crossover_func(
                        population[i], population[i+1])
                    
                    crossedover_indexes.append(i)
                    crossedover_indexes.append(i+1)
                    new_population.append(child1)
                    new_population.append(child2)

            #Mutation to individuals that didn't crossover
            for i in range(self.pop_size):
                if i not in crossedover_indexes and random.random() < self.p_m:
                    mutated = self.mutation_func(
                        population[i], self.helper, self.swap, self.table_flip, self.relationship_augmenter)
                    
                    mutated_indexes.append(i)
                    new_population.append(mutated)

            #Adding the individuals that didn't crossover or mutate
            for i in range(self.pop_size):
                if i not in crossedover_indexes and i not in mutated_indexes:
                    new_population.append(population[i])

            population = new_population[:self.pop_size]

            #Print the best and average fitness of the population
            print(max([self.helper.fitness(individual) for individual in population]),
                  np.mean([self.helper.fitness(individual) for individual in population]))

        best_fitness = max([self.helper.fitness(individual) for individual in population])
        best_individual = population[np.argmax([self.helper.fitness(individual) for individual in population])]

        return best_fitness, best_individual
