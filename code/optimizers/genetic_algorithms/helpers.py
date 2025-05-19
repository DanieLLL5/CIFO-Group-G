from collections import Counter

def repair_solution(child):
    
    # We convert the child to only one list so it's easier to check who is duplicated or missing
    all_guests = [guest for table in child for guest in table]
    
    # We count how many times each guest appears
    guest_counts = Counter(all_guests)
    
    # Identify the duplicate and missing guests
    duplicates = [guest for guest, count in guest_counts.items() if count > 1]
    missing = [guest for guest in range(1, 65) if guest_counts[guest] == 0]
    
    # Return the child if there is no issue
    if not duplicates and not missing:
        return child

    # Convert the solution back to a list of lists 
    repaired_child = [list(table) for table in child]

    dup_index = 0
    miss_index = 0

    seen = set()

    # In this loop we look table by table, guest by guest if we have seen him before
    # if we did it is a duplicate and we substitute it by one of the missing guests
    for table_index, table in enumerate(repaired_child):
        for guest_index, guest in enumerate(table):
            if guest in seen:
                # Inside this condition we will replace every duplicate we find with one missing guest
                # from the last in the list to the first
                new_guest = missing[miss_index]
                repaired_child[table_index][guest_index] = new_guest
                miss_index += 1
            else:
                seen.add(guest)

    return repaired_child
