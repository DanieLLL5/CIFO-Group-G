import random

def mutation(individual, helper, swap=True, table_flip=True, relationship_augmenter=True):

    #The following code takes all mutations that were selected and randomly picks one
    i = 0
    mutations = []
    possible_mutations = [[swap,table_flip,relationship_augmenter],["swap","table_flip","relationship_augmenter"]]
    for mutation in possible_mutations[0]:
        if mutation:
            mutations.append(possible_mutations[1][i])
        i+=1

    #If the user hasn't picked any mutations he will be warned
    if len(mutations) == 0:
        raise ValueError("No mutation method selected. Please select at least one mutation method.")

    mutation = random.choice(mutations)

    if mutation == "swap":

        #here the individual switches to a "neighbouring solution" meaning two people swapped tables
        individual = random.choice(helper.get_neighbours(individual))

    elif mutation == "table_flip":

        '''in this mutation all guests from 1 to 32 and from 33 to 64 swap their assigned tables.
        this means that guest 1 and guest 64 now swap tables, but also
        guests 2 and 63, 3 and 62 and so on will swap tables as well until everyone swapped tables'''


        #with this new way of storing individuals it will be easier to perform the mutation
        #the solution will be stored as the guest number followed by the table they belong to
        individual_transformed=[]

        #will represent the table
        for i in range(len(individual)):
            #will represent the individual
            for j in range(len(individual[i])):
                individual_transformed.append([individual[i][j],i])


        #sorting the guests in their respective order
        individual_transformed.sort(key=helper.sorter2)

        #swapping the tables
        for i in range(int((len(individual_transformed)/2))):
            guest_table1 = individual_transformed[i][1]
            guest_table2 = individual_transformed[-i-1][1]
            individual_transformed[i][1] = guest_table2
            individual_transformed[-i-1][1] = guest_table1

        #lastly we convert back to our 8 lists with 8 guests format
        individual = [[],[],[],[],[],[],[],[]]
        for i in range(len(individual_transformed)):
            individual[individual_transformed[i][1]].append(i+1)

    elif mutation == "relationship_augmenter":
        guest_table = 0
        related_guest_table = 0

        while guest_table == related_guest_table:
            guest_table = random.choice(range(len(individual)))
            guest_seating = random.choice(range(len(individual[guest_table])))
            guest = individual[guest_table][guest_seating]

            related_guest = guest + 1 if guest != 64 else 63

            # Find where the related guest is
            related_guest_found = False
            for i in range(len(individual)):
                for j in range(len(individual[i])):
                    if individual[i][j] == related_guest:
                        related_guest_table = i
                        related_guest_seating = j
                        related_guest_found = True
                        break
                if related_guest_found:
                    break
            else:
                # related_guest was not found, fallback
                raise ValueError(f"Related guest {related_guest} not found in individual.")

        # Swap with someone from related guest table (not the related guest)
        options = [x for x in range(len(individual[related_guest_table])) if x != related_guest_seating]
        if not options:
            raise ValueError("No valid swap candidates found (everyone at the table is the related guest).")

        swapped_guest = individual[related_guest_table][random.choice(options)]
        individual[guest_table].remove(guest)
        individual[related_guest_table].remove(swapped_guest)
        individual[related_guest_table].append(guest)
        individual[guest_table].append(swapped_guest)

    return individual
