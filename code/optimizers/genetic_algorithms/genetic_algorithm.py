import random
import numpy as np
from utils.WeddingSeatingHelper import fitness, generate_solution
from optimizers.genetic_algorithms.selection import selection
from optimizers.genetic_algorithms.mutation import mutation
from optimizers.genetic_algorithms.crossover import crossover

class GeneticAlgorithm:
    def __init__(
        self,
        pop_size=100,
        num_gen=50,
        p_xo=0.8,
        p_m=0.05,
        selection_method="battle",
        elitism=True,
        n_elite=10,
        n_battles=5,
        p_pity=0.0001,
        swap=True,
        table_flip=True,
        relationship_augmenter=True,
        crossover_type="single table swap"
    ):
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
        self.crossover_type = crossover_type

        self.history = []
        self.best_solution = None
        self.best_fitness = float("-inf")

    def optimize(self, verbose=True):
        population = [generate_solution() for _ in range(self.pop_size)]

        for gen in range(self.num_gen):
            if verbose:
                print(f"Generation {gen}")

            # Selection
            selected_population = selection(
                population,
                self.pop_size,
                selection=self.selection_method,
                elitism=self.elitism,
                n_elite=self.n_elite,
                n_battles=self.n_battles,
                p_pity=self.p_pity,
            )

            # Crossover & Mutation
            for i in range(self.pop_size // 2):
                if random.random() < self.p_xo:
                    selected_population[i], selected_population[-i - 1] = crossover(
                        selected_population[i], selected_population[-i - 1],
                        crossover=self.crossover_type
                    )
                elif random.random() < self.p_m * 2:
                    if random.random() < 0.5:
                        selected_population[i] = mutation(
                            selected_population[i],
                            self.swap,
                            self.table_flip,
                            self.relationship_augmenter,
                        )
                    else:
                        selected_population[-i - 1] = mutation(
                            selected_population[-i - 1],
                            self.swap,
                            self.table_flip,
                            self.relationship_augmenter,
                        )

            # Evaluate and track best
            fitnesses = [fitness(ind) for ind in selected_population]
            gen_best_idx = np.argmax(fitnesses)
            gen_best_fit = fitnesses[gen_best_idx]

            if gen_best_fit > self.best_fitness:
                self.best_fitness = gen_best_fit
                self.best_solution = selected_population[gen_best_idx]

            self.history.append(self.best_fitness)
            population = selected_population

            if verbose:
                print(f"Best fitness: {self.best_fitness:.2f} | Avg fitness: {np.mean(fitnesses):.2f}")

        return self.best_fitness, self.best_solution
