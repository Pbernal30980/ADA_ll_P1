import tkinter as tk
from tkinter import messagebox
from smart_terminal.algorithm.transform_string_brute_force import transform_string_brute_force
from smart_terminal.algorithm.transform_string_dp import transform_string_dp
from smart_terminal.algorithm.transform_string_greedy import transform_string_greedy

def calcular():
    try:
        costo_advance = int(entry_advance.get())
        costo_replace = int(entry_replace.get())
        costo_delete = int(entry_delete.get())
        costo_kill = int(entry_kill.get())
        costo_insert = int(entry_insert.get())
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos para los costos.")
        return

    cadena_actual = entry_cadena_actual.get()
    cadena_objetivo = entry_cadena_objetivo.get()

    if not cadena_actual or not cadena_objetivo:
        messagebox.showerror("Error", "Por favor, ingresa las cadenas.")
        return

    # Diccionario de costos
    cost = {
        'advance': costo_advance,
        'replace': costo_replace,
        'delete': costo_delete,
        'kill': costo_kill,
        'insert': costo_insert
    }

    algoritmo = var_algoritmo.get()
    if algoritmo == "Fuerza Bruta":
        min_cost, operations = transform_string_brute_force(cadena_actual, cadena_objetivo, cost)
    elif algoritmo == "Programación Dinámica":
        min_cost, operations = transform_string_dp(cadena_actual, cadena_objetivo, cost)
    elif algoritmo == "Voraz":
        min_cost, operations = transform_string_greedy(cadena_actual, cadena_objetivo, cost)
    else:
        messagebox.showerror("Error", "Selecciona un algoritmo.")
        return

    # Mostrar las operaciones paso a paso
    mostrar_pasos(cadena_actual, operations, cost)

def mostrar_pasos(cadena_actual, operations, cost):
    # Reiniciar el resultado previo
    label_resultado.config(text="")
    paso_actual = 0
    costo_acumulado = 0

    def ejecutar_paso():
        nonlocal paso_actual, cadena_actual, costo_acumulado
        if paso_actual < len(operations):
            operacion = operations[paso_actual]

            if operacion.startswith("advance"):
                cadena_actual = cadena_actual[1:]
                costo_acumulado += cost['advance']
            elif operacion.startswith("replace"):
                cadena_actual = operacion.split()[1] + cadena_actual[1:]
                costo_acumulado += cost['replace']
            elif operacion.startswith("delete"):
                cadena_actual = cadena_actual[1:]
                costo_acumulado += cost['delete']
            elif operacion.startswith("kill"):
                cadena_actual = ""
                costo_acumulado += cost['kill']
            elif operacion.startswith("insert"):
                caracter = operacion.split()[1]
                cadena_actual = caracter + cadena_actual
                costo_acumulado += cost['insert']

            resultado = f"Paso {paso_actual + 1}: {operacion}\nCadena actual: {cadena_actual}\nCosto acumulado: {costo_acumulado}"
            label_resultado.config(text=resultado)

            # Avanzar al siguiente paso después de 1 segundo
            paso_actual += 1
            ventana.after(1000, ejecutar_paso)

    ejecutar_paso()

def abrir_terminal_inteligente():
    global entry_advance, entry_replace, entry_delete, entry_kill, entry_insert
    global entry_cadena_actual, entry_cadena_objetivo, label_resultado, var_algoritmo, ventana

    ventana = tk.Toplevel()
    ventana.title("Terminal Inteligente")

    tk.Label(ventana, text="Costo de Advance:").grid(row=0, column=0)
    entry_advance = tk.Entry(ventana)
    entry_advance.grid(row=0, column=1)

    tk.Label(ventana, text="Costo de Replace:").grid(row=1, column=0)
    entry_replace = tk.Entry(ventana)
    entry_replace.grid(row=1, column=1)

    tk.Label(ventana, text="Costo de Delete:").grid(row=2, column=0)
    entry_delete = tk.Entry(ventana)
    entry_delete.grid(row=2, column=1)

    tk.Label(ventana, text="Costo de Kill:").grid(row=3, column=0)
    entry_kill = tk.Entry(ventana)
    entry_kill.grid(row=3, column=1)

    tk.Label(ventana, text="Costo de Insert:").grid(row=4, column=0)
    entry_insert = tk.Entry(ventana)
    entry_insert.grid(row=4, column=1)

    tk.Label(ventana, text="Cadena Actual (X):").grid(row=5, column=0)
    entry_cadena_actual = tk.Entry(ventana)
    entry_cadena_actual.grid(row=5, column=1)

    tk.Label(ventana, text="Cadena Objetivo (Y):").grid(row=6, column=0)
    entry_cadena_objetivo = tk.Entry(ventana)
    entry_cadena_objetivo.grid(row=6, column=1)

    # Selección de algoritmo
    var_algoritmo = tk.StringVar(value="Fuerza Bruta")
    tk.Label(ventana, text="Seleccionar algoritmo:").grid(row=7, column=0)
    tk.Radiobutton(ventana, text="Fuerza Bruta", variable=var_algoritmo, value="Fuerza Bruta").grid(row=7, column=1)
    tk.Radiobutton(ventana, text="Programación Dinámica", variable=var_algoritmo, value="Programación Dinámica").grid(row=8, column=1)
    tk.Radiobutton(ventana, text="Voraz", variable=var_algoritmo, value="Voraz").grid(row=9, column=1)

    btn_calcular = tk.Button(ventana, text="Calcular", command=calcular)
    btn_calcular.grid(row=10, column=1)

    label_resultado = tk.Label(ventana, text="")
    label_resultado.grid(row=11, column=0, columnspan=2)
