def auction_greedy(A, B, n, offers):
    """
    Transforms the action assignment problem using a greedy algorithm to maximize the total value.
    Args:
        A (int): Total number of actions available.
        B (int): The minimum price to consider a bid as valid.
        n (int): Number of offers.
        offers (list of dict): A list of offers, each containing:
            - 'price': The price of the offer.
            - 'min': The minimum number of actions to assign to the offer.
            - 'max': The maximum number of actions that can be assigned.
    Returns:
        tuple: A tuple containing:
            - best_assignment (list): Optimal assignment of actions to offers.
            - total_value (int): Maximum total value obtained by the assignment.
    """
    valid_offers = [(i, offer) for i, offer in enumerate(offers) if offer['price'] >= B]
    valid_offers.sort(key=lambda x: x[1]['price'], reverse=True)

    total_value = 0
    remaining_actions = A
    best_assignment = [0] * len(offers)

    for offer_index, offer in valid_offers:
        min_amount = offer['min']
        max_amount = offer['max']

        if remaining_actions <= 0:
            break
            
        amount_to_assign = min(max_amount, remaining_actions)
        if amount_to_assign < min_amount:
            continue 

        best_assignment[offer_index] = amount_to_assign
        total_value += amount_to_assign * offer['price']
        remaining_actions -= amount_to_assign

    return best_assignment, total_value