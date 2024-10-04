
# Description: Main file to run the algorithm
from utils.apply_operations import apply_operations
from algorithm.transform_string_dp import transform_string_dp
from algorithm.transform_string_greedy import transform_string_greedy
from algorithm.transform_string_brute_force import transform_string_brute_force


cost = {'advance': 1, 'delete': 2, 'replace': 3, 'insert': 2, 'kill': 1}


base_string =  "algorithm"
target_string = "altruistic"
transformation_cost, transformation_steps = transform_string_dp(base_string, target_string, cost= cost)
print(f"Costo mínimo dp: {transformation_cost}")
print(f"Pasos: {transformation_steps}")
print(f"Resultado final: {apply_operations(base_string, transformation_steps)}")

transformation_cost, transformation_steps = transform_string_greedy(base_string, target_string, cost= cost)
print(f"Costo mínimo greedy: {transformation_cost}")
print(f"Pasos: {transformation_steps}")
print(f"Resultado final: {apply_operations(base_string, transformation_steps)}")


transformation_cost, transformation_steps = transform_string_brute_force(base_string, target_string, cost= cost)
print(f"Costo mínimo fb: {transformation_cost}")
print(f"Pasos: {transformation_steps}")
print(f"Resultado final: {apply_operations(base_string, transformation_steps)}")