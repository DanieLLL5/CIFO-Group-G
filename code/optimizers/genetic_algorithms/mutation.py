import random

def mutation(individual, helper, swap=True, table_flip=True, relationship_augmenter=True):
    """
    Applies a random mutation to an individual based on enabled mutation types.
    
    :param individual: Current solution (list of tables with guests)
    :param helper: An instance of WeddingSeatingHelper
    :param swap: Enable swap mutation
    :param table_flip: Enable table flip mutation
    :param relationship_augmenter: Enable relationship augmenter mutation
    :return: mutated individual
    """
    # Collect enabled mutation types
    mutations = []
    if swap:
        mutations.append("swap")
    if table_flip:
        mutations.append("table_flip")
    if relationship_augmenter:
        mutations.append("relationship_augmenter")

    if not mutations:
        raise ValueError("Please select at least one mutation method.")

    mutation = random.choice(mutations)

    if mutation == "swap":
        # Swap two guests from neighboring solution
        individual = random.choice(helper.get_neighbours(individual))

    elif mutation == "table_flip":
        individual_transformed = []

        for i in range(len(individual)):
            for j in range(len(individual[i])):
                individual_transformed.append([individual[i][j], i])

        individual_transformed.sort(key=helper.sorter2)

        for i in range(len(individual_transformed) // 2):
            i1 = individual_transformed[i]
            i2 = individual_transformed[-i - 1]
            i1[1], i2[1] = i2[1], i1[1]

        new_individual = [[] for _ in range(8)]
        for guest_id, table_id in individual_transformed:
            new_individual[table_id].append(guest_id)

        individual = new_individual

    elif mutation == "relationship_augmenter":
        while True:
            guest_table = random.randint(0, 7)
            guest_seating = random.randint(0, 7)
            guest = individual[guest_table][guest_seating]

            related_guest = guest + 1 if guest != 64 else 63

            related_guest_table = None
            related_guest_seating = None

            for i in range(8):
                for j in range(8):
                    if individual[i][j] == related_guest:
                        related_guest_table = i
                        related_guest_seating = j
                        break
                if related_guest_table is not None:
                    break

            if guest_table != related_guest_table:
                break

        swap_choices = [
            i for i in range(8)
            if i != related_guest_seating
        ]
        swapped_guest = individual[related_guest_table][random.choice(swap_choices)]

        individual[guest_table].remove(guest)
        individual[related_guest_table].remove(swapped_guest)

        individual[related_guest_table].append(guest)
        individual[guest_table].append(swapped_guest)

    return individual
