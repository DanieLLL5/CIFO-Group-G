import copy
from .helpers import repair_solution

def crossover(individual1, individual2, crossover = "single table swap"):
    print(individual1, individual2)
    #This crossover swaps two tables from the parents
    if crossover == "single table swap":
        
        #To solve this problem we need to represent our solution with sets 
        individual1_set = [set(table) for table in individual1]
        individual2_set = [set(table) for table in individual2]
        
        #In these variables we will store the tables amoung parents that are the most similiar but not equal
        #and store how many guests they have in common
        best_pair = None
        most_common_guests = -1
        best_score = -1
        
        for i, table1 in enumerate(individual1_set):
            for j, table2 in enumerate(individual2_set):
                '''we don't want equal tables because when we swap them, 
                we would have solutions that are the same as the parents
                but we also want similiar tables so we don't have to repair as many duplicates
                and missing guests and aren't as destructive to our parent solutions'''
                if table1 != table2:
                    #here we use a set intercection to know what individuals they have in common
                    common = table1 & table2
                    if len(common) > best_score:
                        most_common_guests = len(common)
                        best_score = len(common)
                        #when the loop ends we will have stored the best tables to swap
                        best_pair = (i, j)
        print(best_pair)
        
        #Create children by copying the parent solutions
        child1 = copy.deepcopy(individual1_set)
        child2 = copy.deepcopy(individual2_set)

        #Perform the swap
        i, j = best_pair
        child1[i], child2[j] = child2[j], child1[i]
        
    elif crossover == "table by table":

        #this algorithm starts with empty solutions as children
        #and we add their parents table one at a time
        child1 = []
        child2 = []

        #with this loop tables will be added alternatively to each child
        for table in range(int(len(individual1)/2)):
            child1.append(individual1[table*2])
            child2.append(individual2[table*2])
            child1.append(individual2[table*2+1])
            child2.append(individual1[table*2+1])



    #Now we need to repair the duplicates and missing guests we introduced in the crossovers
        
    child1 = repair_solution(child1)
    child2 = repair_solution(child2)

    return child1, child2
