import unittest

from smart_terminal.algorithm.transform_string_dp import transform_string_dp
from smart_terminal.algorithm.transform_string_brute_force import *
from smart_terminal.algorithm.transform_string_greedy import *

from smart_terminal.utils.apply_operations import apply_operations

class SmartTerminalTest(unittest.TestCase):
    
    def test_algorithm_dynamic_programming(self):
        print("\nTesting dynamic programming algorithm...")
        cost = {'advance': 1, 'delete': 2, 'replace': 3, 'insert': 2, 'kill': 1}
        base_string = "algorithm"
        target_string = "altruistic"
        expected_transformation_cost = 19
        final_cost, steps = transform_string_dp(base_string, target_string, cost)
        self.assertEqual(final_cost, expected_transformation_cost, 'The cost is not correct.')
        self.assertEqual(target_string, apply_operations(base_string, steps), 'The transformation is not correct.')
        base_string = "francesa"
        target_string = "ancestro"
        expected_transformation_cost = 16
        final_cost, steps = transform_string_dp(base_string, target_string, cost)
        self.assertEqual(final_cost, expected_transformation_cost, 'The cost is not correct.')
        self.assertEqual(target_string, apply_operations(base_string, steps), 'The transformation is not correct.')
        base_string = "ingenioso"
        target_string = "ingeniero"
        expected_transformation_cost = 12
        final_cost, steps = transform_string_dp(base_string, target_string, cost)
        self.assertEqual(final_cost, expected_transformation_cost, 'The cost is not correct.')
        self.assertEqual(target_string, apply_operations(base_string, steps), 'The transformation is not correct.')
        



    def test_algorithm_greedy(self):
        print("\nTesting greedy algorithm...")
        cost = {'advance': 1, 'delete': 2, 'replace': 3, 'insert': 2, 'kill': 1}
        base_string = "algorithm"
        target_string = "altruistic"
        _, steps = transform_string_greedy(base_string, target_string, cost)
        self.assertEqual(target_string, apply_operations(base_string, steps), 'The transformation is not correct.')
        base_string = "francesa"
        target_string = "ancestro"
        _, steps = transform_string_greedy(base_string, target_string, cost)
        self.assertEqual(target_string, apply_operations(base_string, steps), 'The transformation is not correct.')
        base_string = "ingenioso"
        target_string = "ingeniero"
        _, steps = transform_string_greedy(base_string, target_string, cost)
        self.assertEqual(target_string, apply_operations(base_string, steps), 'The transformation is not correct.')

    def test_algorithm_brute_force(self):
        print("\nTesting brute force algorithm...")
        cost = {'advance': 1, 'delete': 2, 'replace': 3, 'insert': 2, 'kill': 1}
        base_string = "algorithm"
        target_string = "altruistic"
        expected_transformation_cost = 19
        final_cost, steps = transform_string_brute_force(base_string, target_string, cost)
        self.assertEqual(final_cost, expected_transformation_cost, 'The cost is not correct.')
        self.assertEqual(target_string, apply_operations(base_string, steps), 'The transformation is not correct.')
        base_string = "francesa"
        target_string = "ancestro"
        expected_transformation_cost = 16
        final_cost, steps = transform_string_brute_force(base_string, target_string, cost)
        self.assertEqual(final_cost, expected_transformation_cost, 'The cost is not correct.')
        self.assertEqual(target_string, apply_operations(base_string, steps), 'The transformation is not correct.')
        base_string = "ingenioso"
        target_string = "ingeniero"
        expected_transformation_cost = 12
        final_cost, steps = transform_string_brute_force(base_string, target_string, cost)
        self.assertEqual(final_cost, expected_transformation_cost, 'The cost is not correct.')
        self.assertEqual(target_string, apply_operations(base_string, steps), 'The transformation is not correct.')      



if __name__ == '__main__':
    unittest.main()