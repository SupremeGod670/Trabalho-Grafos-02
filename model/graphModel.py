import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from model.capitalModel import CapitalModel
from model.nodeModel import NodeModel


class Graph:
    def __init__(self):
        self.vertices = {}  # nome: CapitalModel

    def add_vertex(self, name: str, capital: CapitalModel):
        self.vertices[name] = capital

    def add_edge(self, from_name: str, to_name: str, distance: int):
        self.vertices[from_name].neighbors[to_name] = distance

    def show(self):
        for name, capital in self.vertices.items():
            print(f"{name} (Pedágio: {capital.toll}) -> {capital.neighbors}")
