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
    data = request.json
    acciones = data.get('acciones')
    precio_minimo = data.get('precio_minimo')
    n = data.get('ofertas')
    ofertas = data.get('ofertas_detalle')

    algoritmo = data.get('algoritmo')

    if algoritmo == 'brute_force':
        best_assignment, best_price = auction_brute_force(acciones, precio_minimo, n, ofertas)
    elif algoritmo == 'dp':
        best_assignment, best_price = auction_dp(acciones, precio_minimo, n, ofertas)
    else:
        best_assignment, best_price = auction_greedy(acciones, precio_minimo, n, ofertas)
    
    return jsonify({
        'best_assignment': best_assignment,
        'best_price': best_price
    })

@app.route('/transform_string', methods=['POST'])
def transformar_string():
    data = request.json

    cadena_actual = data.get('cadena_actual')
    cadena_objetivo = data.get('cadena_objetivo')

    costos = {
        'advance': data.get('costo_avance'),
        'insert': data.get('costo_insert'),
        'delete': data.get('costo_delete'),
        'replace': data.get('costo_replace'),
        'kill': data.get('costo_kill')
    }

    for key, value in costos.items():
        if value is None:
            return jsonify({'error': f'El costo de {key} no puede estar vacío.'}), 400
        try:
            costos[key] = int(value)
        except ValueError:
            return jsonify({'error': f'El costo de {key} debe ser un número.'}), 400

    algoritmo = data.get('algoritmo')
    
    if algoritmo == 'fuerza_bruta':
        total_cost, steps = transform_string_brute_force(cadena_actual, cadena_objetivo, costos)
    elif algoritmo == 'dinamica':
        total_cost, steps = transform_string_dp(cadena_actual, cadena_objetivo, costos)
    elif algoritmo == 'voraz':
        total_cost, steps = transform_string_greedy(cadena_actual, cadena_objetivo, costos)
    else:
        return jsonify({'error': 'Algoritmo no válido'}), 400

    return jsonify({'costo_total': total_cost, 'pasos': steps})


def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000/')

if __name__ == '__main__':
    open_browser() 
    app.run(debug=True)
