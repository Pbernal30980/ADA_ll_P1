import os
import json
import sys
import time
import math 
import numpy as np
import matplotlib.pyplot as plt

from smart_terminal.algorithm.transform_string_dp import transform_string_dp
from smart_terminal.algorithm.transform_string_brute_force import transform_string_brute_force
from smart_terminal.algorithm.transform_string_greedy import transform_string_greedy

from public_auction.algorithm.auction_brute_force import auction_brute_force
from public_auction.algorithm.auction_dp import auction_dp
from public_auction.algorithm.auction_greedy import auction_greedy

class Benchmark:
    """
    A class to benchmark the execution time of functions over multiple iterations and visualize the results.
    Attributes:
    -----------
    num_iterations : int
        Number of iterations to run each function for benchmarking.
    results : dict
        Dictionary to store the benchmarking results.
    theoretical_costs : dict
        Dictionary to store the theoretical costs for each function and case.
    """
    def __init__(self, num_iterations=50, save_folder='results', prefix=''):
        self.num_iterations = num_iterations
        self.results = {}
        self.save_folder = save_folder
        self.prefix = prefix
        self.theoretical_costs = {}

    def add_function(self, func, case, theoretical_complexity):
        case_name = case['name']
        if case_name not in self.results:
            self.results[case_name] = {}
            self.theoretical_costs[case_name] = {}

        func_name = func.__name__
        self.results[case_name][func_name] = self._benchmark_function(func, *case['args'])
        self.theoretical_costs[case_name][func_name] = theoretical_complexity

    def _benchmark_function(self, func, *args):
        times = []
        for _ in range(self.num_iterations):
            start_time = time.time()
            func(*args)
            end_time = time.time()
            times.append(end_time - start_time)
        return np.array(times)

    def plot_results_per_case(self, log_scale=True):
        for case_name, funcs_times in self.results.items():
            plt.figure(figsize=(10, 6))
            for func_name, times in funcs_times.items():
                plt.plot(times, label=f'{func_name} (mean: {np.mean(times):.6f} s)')

            plt.title(f'Time Execution - {case_name}')
            plt.xlabel('Iteration')
            plt.ylabel('Time (s)')
            plt.legend()
            plt.grid(True)

            if log_scale:
                plt.yscale('log')

            if self.save_folder:
                if not os.path.exists(self.save_folder):
                    os.makedirs(self.save_folder)

                file_path = os.path.join(self.save_folder, self.prefix + case_name.replace(' ', '_').lower() + '.png')
                plt.savefig(file_path)
                print(f'Graph saved in: {file_path}')

    def plot_average_results(self, log_scale=True):
        average_times = {}

        for _, funcs in self.results.items():
            for func_name, times in funcs.items():
                if func_name not in average_times:
                    average_times[func_name] = []
                average_times[func_name].append(np.mean(times))

        overall_averages = {func_name: np.mean(times) for func_name, times in average_times.items()}

        plt.figure(figsize=(10, 6))

        for func_name, times in average_times.items():
            plt.plot(times, label=f'{func_name} (mean: {overall_averages[func_name]:.6f} s)')
      
        plt.title('Average Execution Time per Function Across All Cases')
        plt.xlabel('Case Number')
        plt.ylabel('Average Time (s)')
        plt.xticks(ticks=range(len(self.results)), labels=[f'Case {i + 1}' for i in range(len(self.results))])
        plt.legend()
        plt.grid(True)

        if log_scale:
            plt.yscale('log')

        if self.save_folder:
            if not os.path.exists(self.save_folder):
                os.makedirs(self.save_folder)

            json_path = os.path.join(self.save_folder, self.prefix + 'results_times.json')
            with open(json_path, 'w') as f:
                data = {}
                for func_name, times in average_times.items():
                    if func_name not in data:
                        data[func_name] = {
                            'values': [],
                            'times': []
                        }
                    for time in times:
                        data[func_name]['times'].append(time)
                    case_names = self.results.keys()
                    for case_name in case_names:
                        data[func_name]['values'].append(self.theoretical_costs[case_name][func_name])   
                f.write(json.dumps(data))
               
            file_path = os.path.join(self.save_folder, self.prefix +  'average_results.png')
            plt.savefig(file_path)
            print(f'Average graph saved in: {file_path}')

    def plot_theoretical(self, log_scale=True):
        plt.figure(figsize=(10, 6))

        case_names = list(self.theoretical_costs.keys())
        theoretical_values = {func_name: [] for func_name in next(iter(self.theoretical_costs.values())).keys()}
        
        for case_name in case_names:
            for func_name, cost in self.theoretical_costs[case_name].items():
                theoretical_values[func_name].append(cost)

        for func_name, costs in theoretical_values.items():
            plt.plot(case_names, costs, marker='o', label=f'{func_name} (theoretical)')

            for i, cost in enumerate(costs):
                plt.annotate(f'{cost}', 
                            (case_names[i], cost), 
                            textcoords="offset points", 
                            xytext=(0, 5), 
                            ha='center') 

        plt.title('Theoretical Costs Across Cases')
        plt.xlabel('Case Number')
        plt.ylabel('Theoretical Cost')
        plt.xticks(ticks=range(len(case_names)), labels=[f'Case {i + 1}' for i in range(len(case_names))])
        plt.legend()
        plt.grid(True)

        
        if log_scale:
            plt.yscale('log')
            plt.gca().yaxis.set_visible(False)

        if self.save_folder:
            if not os.path.exists(self.save_folder):
                os.makedirs(self.save_folder)

            file_path = os.path.join(self.save_folder, self.prefix + 'theoretical.png')
            plt.savefig(file_path)
            print(f'Theoretical graph saved in: {file_path}')


if __name__ == '__main__':
    args = sys.argv
    prefix = ''
    
    if len(args) == 1:
        print('Please provide smart_terminal or public_auction as argument')
        sys.exit(1)

    if  args[1] not in ['smart_terminal', 'public_auction']:
        print('Please provide smart_terminal or public_auction as argument')
        sys.exit(1)
    
    print(f'Running benchmark for {args[1]}')

    prefix = args[1] + '_'
        
    benchmark = Benchmark(num_iterations=1000, prefix=prefix)
    cost = {'advance': 1, 'delete': 2, 'replace': 3, 'insert': 2, 'kill': 1}
    A = 100
    B = 10

    string_transform_cases = [
        {
            'name': 'Case empty to empty',
            'args': [' ', ' ', cost],
        },
        {
            'name': 'Case a to ab',
            'args': ['a', 'ab', cost],
        },
        {
            'name': 'Case hola to chao',
            'args': ['bc', 'ab', cost]
        },
        {
            'name': 'Case add to ada',
            'args': ['add', 'ada', cost]
        },
        {
            'name': 'Case hola to holi',
            'args': ['hola', 'holi', cost]
        },
        {
            'name': 'Case perro to gatos',
            'args': ['perro', 'gatos', cost]
        }
    ]

    public_auction_cases = [
        {
            'name': 'Case n = 1',
            'args': [A, B, 1, [{'price': 50, 'min': 40, 'max': 60},
                               {'price': 10, 'min': 0, 'max': 100}]]
        },
        {
            'name': 'Case n = 2',
            'args': [A, B, 2, [{'price': 45, 'min': 10, 'max': 30},
                               {'price': 50, 'min': 40, 'max': 60},
                               {'price': 10, 'min': 0, 'max': 100}]]
        },
        {
            'name': 'Case n = 3',
            'args': [A, B, 3, [{'price': 45, 'min': 10, 'max': 30},
                               {'price': 40, 'min': 10, 'max': 20},
                               {'price': 50, 'min': 40, 'max': 60},
                               {'price': 10, 'min': 0, 'max': 100}]]
        },
        {
            'name': 'Case n = 4',
            'args': [A, B, 4, [{'price': 50, 'min': 40, 'max': 60}, 
                               {'price': 20, 'min': 5, 'max': 10}, 
                               {'price': 40, 'min': 10, 'max': 20}, 
                               {'price': 45, 'min': 10, 'max': 30}, 
                               {'price': 10, 'min': 0, 'max': 100}]]
        },
        {
            'name': 'Case n = 5',
            'args': [A, B, 5, [{'price': 50, 'min': 40, 'max': 60},
                               {'price': 20, 'min': 5, 'max': 10},
                               {'price': 40, 'min': 10, 'max': 20},
                               {'price': 45, 'min': 10, 'max': 30},
                               {'price': 15, 'min': 0, 'max': 10},
                               {'price': 10, 'min': 0, 'max': 100}]]
        }
    ]

    if prefix == 'smart_terminal_':
            for case in string_transform_cases:
                m = len(case['args'][0])
                n = len(case['args'][1])
                benchmark.add_function(transform_string_dp, case,theoretical_complexity=m * n)
                benchmark.add_function(transform_string_brute_force, case, theoretical_complexity=4 ** min(m,n))
                benchmark.add_function(transform_string_greedy, case, theoretical_complexity=m + n)
    else:
        
        for case in public_auction_cases:
            A = case['args'][0]
            n = case['args'][2]
            m = max(offer['max'] for offer in case ['args'][3])
            benchmark.add_function(auction_dp, case, theoretical_complexity=n * (A ** 2))
            benchmark.add_function(auction_brute_force, case, theoretical_complexity=n * (m ** n))
            benchmark.add_function(auction_greedy, case, theoretical_complexity=n * (math.log(n)  if n > 1 else n ))

        

    benchmark.plot_results_per_case()
    benchmark.plot_average_results()
    benchmark.plot_theoretical()