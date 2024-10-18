import os
import json
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def adjust_and_graph_times(times, values, theoretical_func, func_name):
    """
    Adjusts the given times to a theoretical function and plots the experimental and theoretical times.
    Parameters:
    times (list or array-like): The experimental times measured for different input sizes.
    values (list or array-like): The input sizes corresponding to the measured times.
    theoretical_func (callable): The theoretical function to fit the times to. It should take the input sizes as the first argument and the parameters to fit as subsequent arguments.
    func_name (str): The name of the function being analyzed, used for the plot title and saved file name.
    Returns:
    params (array): The parameters of the theoretical function that best fit the experimental times.
    Saves:
    A plot of the experimental and theoretical times as a PNG file in the 'results' directory with the name format '{func_name}_time_complexity.png'.
    """

    params, _ = curve_fit(theoretical_func, values, times)
    
   
    estimated_times = theoretical_func(np.array(values), *params)
    plt.figure(figsize=(10, 6))
    
    plt.plot(values, times, 'ro-', label="Time (experimental)") 
    plt.plot(values, estimated_times, 'b--', label="Time (theoretical)")
    plt.xlabel("Size of input")
    plt.ylabel("Time")
    plt.title(f"Time complexity of {func_name}")
    plt.legend()
   
    file_path = os.path.join('results', func_name + '_time_complexity.png')
    plt.savefig(file_path)
    print(f'Graph saved in: {file_path}')
    return params 

if __name__ == '__main__':
    experiment_results_smart_terminal = None
    experiment_results_public_auction = None
    with open('results/smart_terminal_results_times.json') as f:
        experiment_results_smart_terminal = json.load(f)

    with open('results/public_auction_results_times.json') as f:
        experiment_results_public_auction = json.load(f)

    complexity_functions_smart_terminal = {
        'transform_string_dp' : lambda n, a, b: a * n + b,
        'transform_string_brute_force' : lambda n, a, b: a * n + b,
        'transform_string_greedy' : lambda n, a, b: a * n + b,
    }

    complexity_functions_public_auction = {
        'auction_dp' : lambda n_A2, a, b: a * n_A2 + b,
        'auction_brute_force' : lambda nm_n, a, b: a * nm_n + b,
        'auction_greedy' : lambda n, a, b: a * np.log(n) + b,
    }



    for key in experiment_results_smart_terminal.keys():
        times = experiment_results_smart_terminal[key]['times']
        values = experiment_results_smart_terminal[key]['values']
        params = adjust_and_graph_times(times, values, complexity_functions_smart_terminal[key], key)
        

    for key in experiment_results_public_auction.keys():
        times = experiment_results_public_auction[key]['times']
        values = experiment_results_public_auction[key]['values']
        params = adjust_and_graph_times(times, values, complexity_functions_public_auction[key], key)
