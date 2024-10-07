import time
import numpy as np
import matplotlib.pyplot as plt
import os

from smart_terminal.algorithm.transform_string_dp import transform_string_dp
from smart_terminal.algorithm.transform_string_brute_force import transform_string_brute_force
from smart_terminal.algorithm.transform_string_greedy import transform_string_greedy

class Benchmark:
    """
    A class to benchmark the execution time of functions over multiple iterations and visualize the results.
    Attributes:
    -----------
    num_iterations : int
        Number of iterations to run each function for benchmarking.
    results : dict
        Dictionary to store the benchmarking results.
    Methods:
    --------
    add_function(func, case):
        Adds a function and its test case to the benchmark and runs the benchmark.
    _benchmark_function(func, *args):
        Benchmarks a single function over the specified number of iterations.
    plot_results_per_case(save_folder='results', log_scale=True):
        Plots the execution time of each function for each test case and saves the plots.
    plot_average_results(save_folder='results', log_scale=True):
        Plots the average execution time of each function across all test cases and saves the plot.
    """
    def __init__(self, num_iterations=50):
        self.num_iterations = num_iterations
        self.results = {}

    def add_function(self, func, case):
        
        case_name = case['name']
        if case_name not in self.results:
            self.results[case_name] = {}

        func_name = func.__name__
        self.results[case_name][func_name] = self._benchmark_function(func, *case['args'])

    def _benchmark_function(self, func, *args):
        times = []
        for _ in range(self.num_iterations):
            start_time = time.time()  
            func(*args) 
            end_time = time.time() 
            times.append(end_time - start_time) 
        return np.array(times)

    def plot_results_per_case(self, save_folder='results', log_scale=True):
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

            if save_folder:
                if not os.path.exists(save_folder):
                    os.makedirs(save_folder)

                file_path = os.path.join(save_folder, case_name.replace(' ', '_').lower() + '.png')
                plt.savefig(file_path)
                print(f'Graph saved in: {file_path}')

            plt.show()

    def plot_average_results(self, save_folder='results', log_scale=True):

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

        if save_folder:
            if not os.path.exists(save_folder):
                os.makedirs(save_folder)

            file_path = os.path.join(save_folder, 'average_results.png')
            plt.savefig(file_path)
            print(f'Average graph saved in: {file_path}')



if __name__ == '__main__':
    benchmark = Benchmark()
    cost = {'advance': 1, 'delete': 2, 'replace': 3, 'insert': 2, 'kill': 1}

    string_transform_cases = [
        {
            'name': 'Case add to ada',
            'args': ['add', 'ada', cost]
        },
        {
            'name': 'Case hola to chao',
            'args': ['hola', 'chao', cost]
        },
        {
            'name': 'Case francesa to ancestro',
            'args': ['francesa', 'ancestro', cost]
        },
        {
            'name': 'Case ingenioso to ingeniero',
            'args': ['ingenioso', 'ingeniero', cost]
        },
        {
            'name': 'Case algorithm to altruistic',
            'args': ['algorithm', 'altruistic', cost]
        }
    ]

    for case in string_transform_cases:
        benchmark.add_function(transform_string_dp, case)
        benchmark.add_function(transform_string_brute_force, case)
        benchmark.add_function(transform_string_greedy, case)

    benchmark.plot_results_per_case()

    benchmark.plot_average_results()
