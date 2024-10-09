import tkinter as tk
from public_auction.algorithm.auction_brute_force import auction_brute_force
from public_auction.algorithm.auction_dp import auction_dp
from public_auction.algorithm.auction_greedy import auction_greedy

def abrir_subasta():
    ventana_subasta = tk.Toplevel()
    ventana_subasta.title("Subasta Pública")

    tk.Label(ventana_subasta, text="Número total de acciones (A):").grid(row=0, column=0)
    entry_acciones = tk.Entry(ventana_subasta)
    entry_acciones.grid(row=0, column=1)

    tk.Label(ventana_subasta, text="Precio mínimo (B):").grid(row=1, column=0)
    entry_precio_minimo = tk.Entry(ventana_subasta)
    entry_precio_minimo.grid(row=1, column=1)

    tk.Label(ventana_subasta, text="Número de ofertas (n):").grid(row=2, column=0)
    entry_ofertas = tk.Entry(ventana_subasta)
    entry_ofertas.grid(row=2, column=1)

    oferta_entries = []

    def agregar_ofertas():
        n = int(entry_ofertas.get())

        for i in range(n + 1):
            frame_oferta = tk.Frame(ventana_subasta)
            frame_oferta.grid(row=3 + i, column=0, columnspan=2)

            tk.Label(frame_oferta, text=f"Oferta {i+1} - Precio:").grid(row=0, column=0)
            entry_price = tk.Entry(frame_oferta)
            entry_price.grid(row=0, column=1)

            tk.Label(frame_oferta, text=f"Oferta {i+1} - Min:").grid(row=0, column=2)
            entry_min = tk.Entry(frame_oferta)
            entry_min.grid(row=0, column=3)

            tk.Label(frame_oferta, text=f"Oferta {i+1} - Max:").grid(row=0, column=4)
            entry_max = tk.Entry(frame_oferta)
            entry_max.grid(row=0, column=5)

            oferta_entries.append((entry_price, entry_min, entry_max))

        radio_brute_force.grid_remove()
        radio_dp.grid_remove()
        radio_greedy.grid_remove()

        btn_calcular_subasta.grid(row=3 + n + 1, column=1)
        label_resultado_subasta.grid(row=3 + n + 2, column=0, columnspan=2)

    btn_agregar_ofertas = tk.Button(ventana_subasta, text="Agregar Ofertas", command=agregar_ofertas)
    btn_agregar_ofertas.grid(row=3, column=1)

    algoritmo_var = tk.StringVar(value="greedy")
    radio_brute_force = tk.Radiobutton(ventana_subasta, text="Fuerza Bruta", variable=algoritmo_var, value="brute_force")
    radio_brute_force.grid(row=4, column=0)
    radio_dp = tk.Radiobutton(ventana_subasta, text="Programación Dinámica", variable=algoritmo_var, value="dp")
    radio_dp.grid(row=4, column=1)
    radio_greedy = tk.Radiobutton(ventana_subasta, text="Voraz", variable=algoritmo_var, value="greedy")
    radio_greedy.grid(row=4, column=2)

    def calcular_subasta():
        acciones = int(entry_acciones.get())
        precio_minimo = int(entry_precio_minimo.get())
        n = int(entry_ofertas.get())

        ofertas = []
        for entry_price, entry_min, entry_max in oferta_entries:
            oferta = {
                'price': int(entry_price.get()),
                'min': int(entry_min.get()),
                'max': int(entry_max.get())
            }
            ofertas.append(oferta)

        if algoritmo_var.get() == "brute_force":
            best_assignment, total_value = auction_brute_force(acciones, precio_minimo, n, ofertas)
        elif algoritmo_var.get() == "dp":
            best_assignment, total_value = auction_dp(acciones, precio_minimo, n, ofertas)
        else:
            best_assignment, total_value = auction_greedy(acciones, precio_minimo, n, ofertas)

        resultado = f"Mejor asignación: {best_assignment}, Valor total: {total_value}"
        label_resultado_subasta.config(text=resultado)

    btn_calcular_subasta = tk.Button(ventana_subasta, text="Calcular Subasta", command=calcular_subasta)

    label_resultado_subasta = tk.Label(ventana_subasta, text="")