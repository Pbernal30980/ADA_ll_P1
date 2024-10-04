
def transform_string_brute_force(base_string:str, target_string:str, cost:dict) -> tuple:
    """
    Transforms the base_string into the target_string using a brute-force approach and calculates the minimum cost 
    and the sequence of operations required.
    Args:
        base_string (str): The original string that needs to be transformed.
        target_string (str): The desired string after transformation.
        cost (dict): A dictionary containing the cost of each operation. The keys should be 'insert', 'delete', 
                     'replace', 'advance', and 'kill', and the values should be the respective costs.
    Returns:
        tuple: A tuple containing:
            - total_cost (int): The minimum cost to transform base_string into target_string.
            - operations (list): A list of operations performed to achieve the transformation. Each operation is 
                                 represented as a string, e.g., 'insert a', 'delete', 'replace b', 'advance', 'kill'.
    """
    m = len(base_string)
    n = len(target_string)
    
    def recurse(i, j):
        if i == m and j == n:
            return 0, []
        
        if i == m:
            total_cost = (n - j) * cost['insert']
            operations = [f'insert {target_string[k]}' for k in range(j, n)]
            return total_cost, operations

        if j == n:
            total_cost = (m - i) * cost['delete']
            operations = ['delete' for _ in range(i, m)]
            return total_cost, operations
        if i < m and j < n and base_string[i] == target_string[j]:
            cost_advance, op_advance = recurse(i + 1, j + 1)
            cost_advance += cost['advance']
            op_advance = ['advance'] + op_advance
        else:
            cost_advance, op_advance = float('inf'), []
        
        if i < m and j < n:
            cost_replace, op_replace = recurse(i + 1, j + 1)
            cost_replace += cost['replace']
            op_replace = [f'replace {target_string[j]}'] + op_replace
        else:
            cost_replace, op_replace = float('inf'), []
        
        if j < n:
            cost_insert, op_insert = recurse(i, j + 1)
            cost_insert += cost['insert']
            op_insert = [f'insert {target_string[j]}'] + op_insert
        else:
            cost_insert, op_insert = float('inf'), []
        
        if i < m:
            cost_delete, op_delete = recurse(i + 1, j)
            cost_delete += cost['delete']
            op_delete = ['delete'] + op_delete
        else:
            cost_delete, op_delete = float('inf'), []
        
        if i < m:
            cost_kill = cost['kill'] + ((n - j) * cost['insert'])
            op_kill = ['kill'] + [f'insert {target_string[k]}' for k in range(j, n)]
        else:
            cost_kill, op_kill = float('inf'), []

        min_cost = min(cost_advance, cost_replace, cost_insert, cost_delete, cost_kill)
        if min_cost == cost_advance:
            return cost_advance, op_advance
        elif min_cost == cost_replace:
            return cost_replace, op_replace
        elif min_cost == cost_insert:
            return cost_insert, op_insert
        elif min_cost == cost_delete:
            return cost_delete, op_delete
        else:
            return cost_kill, op_kill

    total_cost, operations = recurse(0, 0)    
    return total_cost, operations
