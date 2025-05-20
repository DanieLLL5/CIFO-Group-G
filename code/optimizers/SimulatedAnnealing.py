import numpy as np
import random
import math

class SimulatedAnnealingOptimizer:
    def __init__(self, helper, L=200, k=1.1, c=1000000, stop=5, seed=42, initial_solution=None):

        """
        :param helper: An instance of WeddingSeatingHelper
        :param L: Number of temperature iterations
        :param k: Cooling rate divisor
        :param c: Initial temperature
        :param stop: Early stop count for no improvement
        :param seed: Random seed for reproducibility
        :param initial_solution: Optional custom starting solution
        """
        self.helper = helper
        self.L = L
        self.k = k
        self.c = c
        self.stop = stop
        self.initial_solution = initial_solution  # This line is essential
        if seed is not None:
            np.random.seed(seed)

    def run(self, verbose=False):
        current_sol = self.initial_solution if self.initial_solution is not None else self.helper.generate_solution()

        count = 0
        temperature = self.c

        for _ in range(self.L):
            current_fit = self.helper.fitness(current_sol)
            neighbours = self.helper.get_neighbours(current_sol)
            neighbours_fitness = [(n, self.helper.fitness(n)) for n in neighbours]
            neighbours_fitness.sort(key=lambda x: x[1], reverse=True)

            for neighbour, neighbour_fit in neighbours_fitness:
                delta = neighbour_fit - current_fit
                # Accept if neighbour is better or with probability exp(delta/temperature)
                if delta > 0 or random.random() < math.exp(delta / temperature):
                    current_sol = neighbour
                    break

            new_fit = self.helper.fitness(current_sol)
            if new_fit <= current_fit:
                count += 1
            else:
                count = 0  # Reset if improvement

            if count >= self.stop:
                break

            if verbose:
                print(f"Current fitness: {new_fit}")

            temperature /= self.k

        return self.helper.fitness(current_sol), current_sol
