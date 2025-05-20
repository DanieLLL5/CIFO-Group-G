import numpy as np
import random
import math

class SimulatedAnnealingOptimizer:
    def __init__(self, helper, L=200, k=1.1, c=1000000, stop=5, seed=None):
        """
        :param helper: An instance of WeddingSeatingHelper
        :param L: Number of temperature iterations
        :param k: Cooling rate divisor
        :param c: Initial temperature
        :param stop: Early stop count for no improvement
        :param seed: Random seed for reproducibility
        """
        self.helper = helper
        self.L = L
        self.k = k
        self.c = c
        self.stop = stop
        if seed is not None:
            np.random.seed(seed)

    def run(self, verbose=False):
        current_sol = self.helper.generate_solution()
        count = 0
        temperature = self.c

        for _ in range(self.L):
            current_fit = self.helper.fitness(current_sol)
            neighbours = self.helper.get_neighbours(current_sol)
            neighbours_fitness = [(n, self.helper.fitness(n)) for n in neighbours]
            neighbours_fitness.sort(key=self.helper.sorter, reverse=True)

            for neighbour, neighbour_fit in neighbours_fitness:
                delta = abs(current_fit - neighbour_fit)
                if random.random() < math.exp(delta / temperature):
                    current_sol = neighbour
                    break

            if current_fit >= self.helper.fitness(current_sol):
                count += 1
            else:
                count = 0  # Reset if improvement

            if count == self.stop:
                break

            if verbose:
                print(f"Current fitness: {self.helper.fitness(current_sol)}")

            temperature /= self.k

        return self.helper.fitness(current_sol), current_sol
