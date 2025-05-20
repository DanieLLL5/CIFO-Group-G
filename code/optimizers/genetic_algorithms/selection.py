import numpy as np
import random

def selection(population, pop_size, helper, selection="battle", elitism=False, n_elite=10, n_battles=5, p_pity=0.0001):
    
    selected_population = []
    individual_fitnesses = []
    
    # getting every individual and their fitness
    for individual in population:
        individual_fitnesses.append([individual, helper.fitness(individual)])
        
    # sorting them from best to worst in terms of fitness
    individual_fitnesses.sort(key=helper.sorter, reverse=True)
    
    # Passing automatically through selection the top individuals if elitism is applied
    if elitism:
        for i in range(n_elite):
            selected_population.append(individual_fitnesses[i][0])
    
    total_fitness = sum([helper.fitness(individual) for individual in population])
    
    # applying selection to our population until it meets the population size
    while len(selected_population) < pop_size:
        
        if selection == "battle":
        
            '''for each individual at a time, from the most fit to the least fit,
            they will be compared to random individuals. 
            the more they "win" (have a higher fitness than the random individual) 
            the more likely they are to pass through selection.
            if they lose all "battles", 
            they still have a small chance of passing selection called probability of pity'''
        
            for j in range(pop_size):
                count = 0
                for battle in range(n_battles):
                    if individual_fitnesses[j][1] > individual_fitnesses[np.random.choice(range(pop_size))][1]:
                        count += 1
                    
                if random.random() < count / n_battles:
                    selected_population.append(individual_fitnesses[j][0])
                
                elif random.random() < p_pity:
                    selected_population.append(individual_fitnesses[j][0])

    
        elif selection == "double_roullette":

            '''This simple selection algorithm randomly selects an individual
            and passes him through selection with propability equal to 
            the percentage of fitness score it has of the total population.
            If he does not pass this test (which might be impossible if he as a fitness between -3000 and 0 (it is possible))
            he still has a pity chance of passing trough the next stage'''
            
            random_individual = population[random.choice(range(pop_size))]
            if helper.fitness(random_individual) / total_fitness > random.random():
                selected_population.append(random_individual)
            elif random.random() < p_pity:
                selected_population.append(random_individual)
        

        else:
            raise ValueError("Invalid selection method. Choose 'battle' or 'double_roullette'.")
        
    # return the selected individuals
    return selected_population
