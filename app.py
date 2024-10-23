import webbrowser
from flask import Flask, request, jsonify, send_from_directory
import sys
import os

sys.path.insert(0, os.path.abspath('..'))

from public_auction.algorithm.auction_brute_force import auction_brute_force
from public_auction.algorithm.auction_dp import auction_dp
from public_auction.algorithm.auction_greedy import auction_greedy
from smart_terminal.algorithm.transform_string_brute_force import transform_string_brute_force
from smart_terminal.algorithm.transform_string_dp import transform_string_dp
from smart_terminal.algorithm.transform_string_greedy import transform_string_greedy

app = Flask(__name__)

@app.route('/')
def serve_frontend():
    return send_from_directory('frontend', 'index.html')

@app.route('/<path:path>')
def send_static(path):
    return send_from_directory('frontend', path)

@app.route('/auction', methods=['POST'])
def calcular_subasta():
    try:
        data = request.json
        actions = data.get('actions')
        min_price = data.get('minPrice')
        n = data.get('offers')
        offers = data.get('detailsOffers') 

        algorithm = data.get('algorithm')

        if algorithm == 'brute_force':
            best_assignment, best_price = auction_brute_force(actions, min_price, n, offers)
        elif algorithm == 'dp':
            best_assignment, best_price = auction_dp(actions, min_price, n, offers)
        else:
            best_assignment, best_price = auction_greedy(actions, min_price, n, offers)
        
        return jsonify({
            'best_assignment': best_assignment,
            'best_price': best_price
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/transform_string', methods=['POST'])
def transform_string():
    data = request.json

    current_string = data.get('current_string')
    target_string = data.get('target_string')

    costs = {
        'advance': data.get('cost_advance'),
        'insert': data.get('cost_insert'),
        'delete': data.get('cost_delete'),
        'replace': data.get('cost_replace'),
        'kill': data.get('cost_kill')
    }

    for key, value in costs.items():
        if value is None:
            return jsonify({'error': f'The cost of {key} cannot be empty.'}), 400
        try:
            costs[key] = int(value)
        except ValueError:
            return jsonify({'error': f'The cost of {key} must be a number.'}), 400

    algorithm = data.get('algorithm')
    
    if algorithm == 'brute_force':
        total_cost, steps = transform_string_brute_force(current_string, target_string, costs)
    elif algorithm == 'dynamic':
        total_cost, steps = transform_string_dp(current_string, target_string, costs)
    elif algorithm == 'greedy':
        total_cost, steps = transform_string_greedy(current_string, target_string, costs)
    else:
        return jsonify({'error': 'Invalid algorithm'}), 400

    return jsonify({'total_cost': total_cost, 'steps': steps})



def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000/')

if __name__ == '__main__':
    open_browser() 
    app.run(debug=True)
