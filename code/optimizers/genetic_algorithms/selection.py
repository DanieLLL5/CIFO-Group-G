import numpy as np
import random

def selection(population, pop_size, helper, selection="battle", elitism=False, n_elite=10, n_battles=5, p_pity=0.0001):
    selected_population = []
    individual_fitnesses = []

    # Getting every individual and their fitness
    for individual in population:
        individual_fitnesses.append([individual, helper.fitness(individual)])

    # Sorting them from best to worst in terms of fitness
    individual_fitnesses.sort(key=lambda x: x[1], reverse=True)

    # Elitism
    if elitism:
        for i in range(n_elite):
            selected_population.append(individual_fitnesses[i][0])

    total_fitness = sum(f for _, f in individual_fitnesses)

    while len(selected_population) < pop_size:
        if selection == "battle":
            for j in range(pop_size):
                count = 0
                for _ in range(n_battles):
                    opponent_index = np.random.choice(range(pop_size))
                    if individual_fitnesses[j][1] > individual_fitnesses[opponent_index][1]:
                        count += 1
                if random.random() < count / n_battles:
                    selected_population.append(individual_fitnesses[j][0])
                elif random.random() < p_pity:
                    selected_population.append(individual_fitnesses[j][0])

        elif selection == "double_roullette":
            random_individual = population[random.choice(range(pop_size))]
            indiv_fit = helper.fitness(random_individual)
            if total_fitness > 0 and indiv_fit / total_fitness > random.random():
                selected_population.append(random_individual)
            elif random.random() < p_pity:
                selected_population.append(random_individual)

    return selected_population
