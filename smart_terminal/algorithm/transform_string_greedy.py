def transform_string_greedy(base_string:str, target_string:str, cost:dict) -> tuple:
    """
    Transforms the base_string into the target_string using a greedy algorithm and calculates the total cost.
    Parameters:
    base_string (str): The original string that needs to be transformed.
    target_string (str): The desired string after transformation.
    cost (dict): A dictionary containing the costs of different operations:
        - 'advance': Cost to advance to the next character if characters match.
        - 'replace': Cost to replace a character in base_string with a character from target_string.
        - 'insert': Cost to insert a character from target_string into base_string.
        - 'delete': Cost to delete a character from base_string.
        - 'kill': Cost to kill the remaining characters in base_string if target_string is exhausted.
    Returns:
    tuple: A tuple containing:
        - total_cost (int): The total cost of transforming base_string into target_string.
        - operations (list): A list of operations performed to achieve the transformation.
    """
    m = len(base_string)
    n = len(target_string)

    i = 0
    j =  0
    total_cost = 0
    operations = []

    while i < m or j < n:
        if i == m:
            operations.append(f'insert {target_string[j]}')
            total_cost += cost['insert']
            j += 1
            continue

        if j == n:
            if cost['delete'] * (m - i) < cost['kill']:
                operations.append('delete')
                total_cost += cost['delete']
                i += 1
            else:
                operations.append('kill')
                total_cost += cost['kill']
                break
            continue

       
        if base_string[i] == target_string[j]:
            if cost['advance'] < cost['replace']:
                operations.append('advance')
                total_cost += cost['advance']
            else:
                operations.append(f'replace {target_string[j]}')
                total_cost += cost['replace']
            i += 1
            j += 1
        else:

            if cost['replace'] <= cost['delete'] and cost['replace'] <= cost['insert'] and cost['replace'] <= cost['delete'] + cost['insert']:
                operations.append(f'replace {target_string[j]}')
                total_cost += cost['replace']
                i += 1
                j += 1
            elif cost['delete'] + cost['insert'] <= cost['replace']:
                operations.append('delete')
                total_cost += cost['delete']
                i += 1
                operations.append(f'insert {target_string[j]}')
                total_cost += cost['insert']
                j += 1
            else:
                operations.append(f'insert {target_string[j]}')
                total_cost += cost['insert']
                j += 1

    return total_cost, operations
