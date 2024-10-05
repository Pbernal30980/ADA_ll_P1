def transform_string_brute_force(base_string, target_string, cost):
    def brute_force(base_string:str, target_string:str, i:int, j:int):
        m, n = len(base_string), len(target_string)
        if i == m and j == n:
            return 0, []
        
        if i == m:
            return (n - j) * cost['insert'], [f'insert {target_string[j]}' for j in range(j, n)]
        
        if j == n:
            if  m * cost['delete'] < cost['kill']:
                return (m - i) * cost['delete'], ['delete']
            else:
                return cost['kill'], ['kill']
            
        cost_replace =  brute_force(base_string, target_string, i + 1, j + 1)
        cost_insert = brute_force(base_string, target_string, i, j + 1)
        cost_delete = brute_force(base_string, target_string, i + 1, j)
        cost_kill = cost['kill'] + (n - j ) * cost['insert'], ['kill'] + [f'insert {target_string[k]}' for k in range(j, n)]

        if base_string[i] == target_string[j]:
            if cost['advance'] < cost['replace']:
                cost_advance = brute_force(base_string, target_string, i + 1, j + 1)
                return cost_advance[0] + cost['advance'], ['advance'] + cost_advance[1]
            else:
                return cost_replace[0] + cost['replace'], [f'replace {target_string[j]}'] + cost_replace[1]

        minimum_cost = min(
            cost_replace[0] + cost['replace'],
            cost_insert[0] + cost['insert'],
            cost_delete[0] + cost['delete'],
            cost_kill[0]
        )

        if minimum_cost == cost_replace[0] + cost['replace']:
            return minimum_cost, [f'replace {target_string[j]}'] + cost_replace[1]
        elif minimum_cost == cost_insert[0] + cost['insert']:
            return minimum_cost, [f'insert {target_string[j]}'] + cost_insert[1]
        elif minimum_cost == cost_delete[0] + cost['delete']:
            return minimum_cost, ['delete'] + cost_delete[1]
        else:
            return minimum_cost, ['kill'] + cost_kill[1]
    
    return brute_force(base_string, target_string, 0, 0)