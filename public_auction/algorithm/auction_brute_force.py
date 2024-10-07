def auction_brute_force(A, B, n, offers):
    def calculate_value(assignment):
        total_value = 0
        remaining_actions = A
        
        for i in range(n):
            if offers[i]['price'] >= B:
                total_value += assignment[i] * offers[i]['price']
                remaining_actions -= assignment[i]
        
        total = total_value + offers[n]['price'] * remaining_actions
        
        return total

    best_assignment = None
    best_total_value = 0

    def combine(i, remaining_actions, current_assignment):
        nonlocal best_assignment, best_total_value
        if i == n:  
            current_assignment[i] = remaining_actions  
            total_value = calculate_value(current_assignment)
            if total_value > best_total_value:
                best_total_value = total_value
                best_assignment = current_assignment[:]
            return

        if offers[i]['price'] < B:
            combine(i + 1, remaining_actions, current_assignment)
            return

        min_actions = offers[i]['min']
        max_actions = min(offers[i]['max'], remaining_actions)
        
        for x in range(min_actions, max_actions + 1):
            current_assignment[i] = x
            combine(i + 1, remaining_actions - x, current_assignment)
        
        current_assignment[i] = 0
        combine(i + 1, remaining_actions, current_assignment)

    combine(0, A, [0] * (n + 1))

    if best_assignment is None:
        best_assignment = [0] * (n + 1)

    total = calculate_value(best_assignment)

    return best_assignment, total


