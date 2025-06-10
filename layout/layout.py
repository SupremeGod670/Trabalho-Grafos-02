import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.graphConstructor import seed_graph
from src.dijkstra import dijkstra

# Carrega o grafo
graph = seed_graph()
capitais = list(graph.vertices.keys())

# Cria a janela principal
root = tk.Tk()
root.title("Trabalho Grafo - 02")
root.geometry("400x500")

label = tk.Label(root, text="Trabalho Sobre o Caminho Mais Barato Entre Capitais!")
label.pack(pady=20)

capital_label1 = tk.Label(root, text="Selecione a capital de origem:")
capital_label1.pack(pady=5)
capital_origin = ttk.Combobox(root, values=capitais, state="readonly")
capital_origin.pack(pady=5)

capital_label2 = tk.Label(root, text="Selecione a capital de destino:")
capital_label2.pack(pady=5)
capital_destiny = ttk.Combobox(root, values=capitais, state="readonly")
capital_destiny.pack(pady=5)

fuel_label = tk.Label(root, text="Preço do combustível (R$/litro):")
fuel_label.pack(pady=5)
fuel_entry = tk.Entry(root)
fuel_entry.pack(pady=5)

auto_label = tk.Label(root, text="Autonomia do veículo (km/l):")
auto_label.pack(pady=5)
auto_entry = tk.Entry(root)
auto_entry.pack(pady=5)

result_label = tk.Label(root, text="", wraplength=380)
result_label.pack(pady=10)

def buscar_caminho():
    origem = capital_origin.get()
    destino = capital_destiny.get()
    if not origem or not destino:
        messagebox.showerror("Erro", "Selecione as capitais de origem e destino.")
        return
    try:
        preco_combustivel = float(fuel_entry.get())
        autonomia = float(auto_entry.get())
    except ValueError:
        messagebox.showerror("Erro", "Insira valores válidos para combustível e autonomia.")
        return
    caminho, custo = dijkstra(graph, origem, destino, preco_combustivel, autonomia)
    if not caminho or custo == float('inf'):
        result_label.config(text="Não foi possível encontrar um caminho.")
    else:
        rota = " → ".join(caminho)
        result_label.config(text=f"Caminho: {rota}\nCusto total: R$ {custo:.2f}")

button = tk.Button(root, text="Buscar Caminho Mais Barato", command=buscar_caminho)
button.pack(pady=20)

root.mainloop()