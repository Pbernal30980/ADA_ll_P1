
def transform_string_dp(base_string:str, target_string:str, cost:dict) -> tuple:
    """
    Transforms the base_string into the target_string using dynamic programming
    to minimize the cost of operations. The operations and their respective costs
    are provided in the cost dictionary.
    Args:
        base_string (str): The initial string to be transformed.
        target_string (str): The desired string after transformation.
        cost (dict): A dictionary containing the cost of each operation:
            - 'advance': Cost of advancing to the next character if characters match.
            - 'replace': Cost of replacing a character in base_string with a character in target_string.
            - 'delete': Cost of deleting a character from base_string.
            - 'insert': Cost of inserting a character from target_string into base_string.
            - 'kill': Cost of deleting all remaining characters in base_string.
    Returns:
        tuple: A tuple containing:
            - int: The minimum cost to transform base_string into target_string.
            - list: A list of operations to achieve the transformation.
    """
    m = len(base_string)
    n = len(target_string)
    dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
    op = [[' ' for _ in range(n + 1)] for _ in range(m + 1)]
    dp[m][n] = 0

    for i in range(m, -1, -1):
        if m * cost['delete']   <  cost['kill']:
            dp[i][n] = m - i * cost['delete']
            op[i][n] = 'delete'
        else:
            dp[i][n] = cost['kill']
            op[i][n] = 'kill'

    for j in range(n, -1 if n > 0 else 0, -1):
        dp[m][j] = (n - j) * cost['insert']
        op[m][j] = f'insert {target_string[j - n]}'

    for i in range(m, -1, -1):
        for j in range(n, -1, -1):
            if i == m or j == n:
                continue
           
            if base_string[i] == target_string[j]:
                cost_advance = dp[i + 1][j + 1] + cost['advance']
                cost_replace = dp[i + 1][j + 1] + cost['replace']
                dp[i][j] = min(dp[i][j], cost_advance, cost_replace)
                if dp[i][j] == cost_advance:
                    op[i][j] = 'advance'
                elif dp[i][j] == cost_replace:
                    op[i][j] = f'replace {target_string[j]}'
                continue
                

            cost_replace = dp[i + 1][j + 1] + cost['replace']
            cost_delete = dp[i + 1][j] + cost['delete']
            cost_insert = dp[i][j + 1] + cost['insert']
            cost_kill = dp[i + 1][j] + cost['kill'] + ((n - j) * cost['insert'])

            dp[i][j] = min(
                cost_replace,
                cost_delete,
                cost_insert,
                cost_kill
            )

            if dp[i][j] == cost_replace:
                op[i][j] = f'replace {target_string[j]}'
            elif dp[i][j] == cost_delete:
                op[i][j] = 'delete'
            elif dp[i][j] == cost_insert:
                op[i][j] = f'insert {target_string[j]}'
            elif dp[i][j] == cost_kill:
                op[i][j] = 'kill'
    steps = build_operation_steps(op, m, n)
    return dp[0][0], steps

def build_operation_steps(op:list, m:int, n:int) -> list:
    """
    Constructs a list of operation steps to transform one string into another based on a given operation matrix.
    Args:
        op (list of list of str): A 2D list where each element represents an operation to be performed.
        m (int): The number of rows in the operation matrix.
        n (int): The number of columns in the operation matrix.
    Returns:
        list of str: A list of operations that describe the steps to transform the source string into the target string.
    """
    i, j = 0, 0
    steps = []
    while i < m or j < n:
        operation = op[i][j]
        steps.append(operation)
        
        if operation.startswith('advance'):
            i += 1
            j += 1
        elif operation.startswith('replace'):
            i += 1
            j += 1
        elif operation.startswith('delete'):
            i += 1
        elif operation.startswith('insert'):
            j += 1
        elif operation.startswith('kill'):
            i += 1
            if op[i][j] == 'kill':
                break
        
    return steps
