import numpy as np
import random
import math

class SimulatedAnnealingOptimizer:
    def __init__(self, helper, L=200, k=1.1, c=1000000, stop=5, seed=None, initial_solution=None):
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
	self.initial_solution = initial_solution
        if seed is not None:
            np.random.seed(seed)

    def run(self, verbose=False):
        current_sol = self.initial_solution if self.initial_solution is not None else self.helper.generate_solution()
        count = 0
        temperature = self.c

        for _ in range(self.L):
            current_fit = self.helper.fitness(current_sol)
	    #Storing the neighbours of our solution
            neighbours = self.helper.get_neighbours(current_sol)
	    #Making a list of all the neighbours and their fitnesses
            neighbours_fitness = [(n, self.helper.fitness(n)) for n in neighbours]
	    #Sorting the neighbours by descending fitness
            neighbours_fitness.sort(key=self.helper.sorter, reverse=True)

            #Deciding if our current solution should switch with the most fit individual
            #And then second, and then the third... Until it switches
            #The more fit the solution, the higher the likelihood of switching
            for neighbour, neighbour_fit in neighbours_fitness:
                delta = abs(current_fit - neighbour_fit)
                if random.random() < math.exp(delta / temperature):
                    current_sol = neighbour
                    break
	    #By doing this we make sure the algorithm isn't stuck and after not improving for too long it stops
            if current_fit >= self.helper.fitness(current_sol):
                count += 1
            else:
                count = 0  # Reset if improvement

            if count == self.stop:
                break

            if verbose:
                print(f"Current fitness: {self.helper.fitness(current_sol)}")
            #Here we increase the chance of switching with the fittest solution
            temperature /= self.k

	    #return the best fitness and solution found at the end of the loop
        return self.helper.fitness(current_sol), current_sol
