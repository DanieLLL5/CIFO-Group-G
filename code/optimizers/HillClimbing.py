import numpy as np

class HillClimbingOptimizer:
    def __init__(self, helper):
        """
        :param helper: An instance of WeddingSeatingHelper or similar class providing necessary methods
        """
        self.helper = helper

    def run(self, verbose=False):
        """
        Run the hill climbing optimization.
        
        :param verbose: If True, prints fitness progress.
        :return: tuple(best_fitness, best_solution)
        """
        current_sol = self.helper.generate_solution()
        neighbours = self.helper.get_neighbours(current_sol)
        neighbour_best_fit = max([self.helper.fitness(neighbour) for neighbour in neighbours])

        while self.helper.fitness(current_sol) < neighbour_best_fit:
            current_sol = neighbours[np.argmax([self.helper.fitness(neighbour) for neighbour in neighbours])]
            neighbours = self.helper.get_neighbours(current_sol)
            neighbour_best_fit = max([self.helper.fitness(neighbour) for neighbour in neighbours])

            if verbose:
                print(f"Current fitness: {self.helper.fitness(current_sol)}")

        return self.helper.fitness(current_sol), current_sol
