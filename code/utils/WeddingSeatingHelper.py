import copy
import numpy as np

class WeddingSeatingHelper:
    def __init__(self, relationships):
        """
        Initialize with the relationships matrix.
        :param relationships: 2D numpy array or nested list with relationship scores.
        """
        self.relationships = relationships

    def get_neighbours(self, solution):
        """
        Generate all unique neighbours by swapping two guests from different tables.
        :param solution: List of lists, each inner list is a table with guests.
        :return: List of neighbour solutions.
        """
        neighbours = []
        for i in range(len(solution) - 1):
            for j in range(len(solution[i])):
                for a in range(i + 1, len(solution)):
                    for b in range(len(solution[a])):
                        neighbour = copy.deepcopy(solution)
                        guest1 = neighbour[i][j]
                        guest2 = neighbour[a][b]

                        # Swap guests
                        neighbour[i].remove(guest1)
                        neighbour[a].remove(guest2)
                        neighbour[i].append(guest2)
                        neighbour[a].append(guest1)

                        neighbours.append(neighbour)
        return neighbours

    @staticmethod
    def sorter(item):
        """
        Helper function to sort by fitness (assumed to be second element in tuple).
        :param item: Tuple or list where fitness is at index 1.
        :return: fitness value
        """
        return item[1]

    @staticmethod
    def sorter2(item):
        """
        Helper function to sort by guest order (assumed to be first element).
        :param item: Tuple or list where guest order is at index 0.
        :return: guest order
        """
        return item[0]

    @staticmethod
    def generate_solution():
        """
        Generate a random initial seating solution.
        :return: List of 8 tables, each with 8 guests.
        """
        guests = np.random.choice(range(1, 65), size=64, replace=False)
        solution = [list(guests[i:i + 8]) for i in range(0, 64, 8)]
        return solution

    def fitness(self, solution):
        """
        Calculate the fitness score of a seating arrangement.
        :param solution: List of tables with guests.
        :return: fitness score (int or float)
        """
        total_fitness = 0
        for table in solution:
            for i in range(len(table)):
                for j in range(i + 1, len(table)):
                    total_fitness += self.relationships[table[i]][table[j]]
        return total_fitness