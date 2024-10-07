def auction_dp(A, B, n, offers):
    prices = [offers[i]['price'] for i in range(n)]
    mins = [offers[i]['min'] for i in range(n)]
    maxs = [offers[i]['max'] for i in range(n)]

    dp = [[0] * (A + 1) for _ in range(n + 1)]

    for i in range(n):
        for a in range(A + 1):
            dp[i + 1][a] = dp[i][a]
            if prices[i] >= B:
                for x in range(mins[i], min(maxs[i], a) + 1):
                    if a >= x:
                        dp[i + 1][a] = max(dp[i + 1][a], dp[i][a - x] + x * prices[i])

    remaining_actions = A
    best_assignment = [0] * (n + 1)

    for i in range(n - 1, -1, -1):
        if prices[i] < B:
            continue
        for x in range(mins[i], min(maxs[i], remaining_actions) + 1):
            if remaining_actions >= x and dp[i + 1][remaining_actions] == dp[i][remaining_actions - x] + x * prices[i]:
                best_assignment[i] = x
                remaining_actions -= x
                break

    if remaining_actions > 0:
        best_assignment[n] = remaining_actions 

    total_value = dp[n][A] + (offers[n]['price'] * best_assignment[n]) 
    return best_assignment, total_value