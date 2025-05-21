import random
import numpy as np

class GeneticAlgorithm:
    def __init__(self, helper, pop_size=100, num_gen=50, p_xo=0.8, p_m=0.05, selection_method="battle",
                 elitism=False, n_elite=10, n_battles=5, p_pity=0.0001,
                 swap=True, table_flip=True, relationship_augmenter=True):
        """
        Initialize the genetic algorithm.

        :param helper: Helper object/class with fitness, generate_solution, selection, crossover, and mutation methods
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

    def run(self):
        # Generate initial population
        population = [self.helper.generate_solution() for _ in range(self.pop_size)]

        for gen in range(self.num_gen):
            print(f"Generation {gen}")

            # Evaluate fitness
            fitnesses = [self.helper.fitness(ind) for ind in population]
            best_fitness = max(fitnesses)
            avg_fitness = np.mean(fitnesses)
            print(f"Best: {best_fitness}, Average: {avg_fitness}")

            # Elitism: preserve best individuals
            elites = []
            if self.elitism:
                elite_indices = np.argsort(fitnesses)[-self.n_elite:]
                elites = [population[i] for i in elite_indices]

            # Selection
            selected_population = self.helper.selection(
                population,
                self.pop_size,
                self.helper,
                selection=self.selection_method,
                elitism=self.elitism,
                n_elite=self.n_elite,
                n_battles=self.n_battles,
                p_pity=self.p_pity
            )

            # Generate new population through crossover and mutation
            new_population = []

            for i in range(0, self.pop_size - 1, 2):
                parent1, parent2 = selected_population[i], selected_population[i + 1]

                if random.random() < self.p_xo:
                    child1, child2 = self.helper.crossover(parent1, parent2)
                else:
                    child1, child2 = parent1, parent2

                if random.random() < self.p_m:
                    child1 = self.helper.mutation(child1, self.helper, self.swap, self.table_flip, self.relationship_augmenter)
                if random.random() < self.p_m:
                    child2 = self.helper.mutation(child2, self.helper, self.swap, self.table_flip, self.relationship_augmenter)

                new_population.extend([child1, child2])

            # If population size is odd, handle the last individual
            if len(new_population) < self.pop_size:
                leftover = selected_population[-1]
                if random.random() < self.p_m:
                    leftover = self.helper.mutation(leftover, self.helper, self.swap, self.table_flip, self.relationship_augmenter)
                new_population.append(leftover)

            # Add elites if elitism is enabled
            if self.elitism:
                new_population = elites + new_population
                new_population = new_population[:self.pop_size]

            population = new_population

        # Final fitness evaluation
        fitnesses = [self.helper.fitness(ind) for ind in population]
        best_fitness = max(fitnesses)
        best_individual = population[np.argmax(fitnesses)]

        return best_fitness, best_individual
