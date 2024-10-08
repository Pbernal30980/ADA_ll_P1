import tkinter as tk
import public_auction.algorithm as pa
import smart_terminal.algorithm as st

ventana_principal = tk.Tk()
ventana_principal.title("Terminal Inteligente y Subasta Pública")

tk.Label(ventana_principal, text="Elige qué interfaz deseas ejecutar:").pack(pady=10)

btn_terminal = tk.Button(ventana_principal, text="Terminal Inteligente", command=st.abrir_terminal_inteligente)
btn_terminal.pack(pady=5)

btn_subasta = tk.Button(ventana_principal, text="Subasta Pública", command=pa.abrir_subasta)
btn_subasta.pack(pady=5)

ventana_principal.mainloop()
