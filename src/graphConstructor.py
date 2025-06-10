import json
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from model.capitalModel import CapitalModel
from model.graphModel import Graph


def GraphConstructor():
    # Caminho correto para o arquivo JSON
    file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..", "data", "capitais.json")
    file_path = os.path.normpath(file_path)

    
    # Abrindo o arquivo JSON
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Transformar em lista de CapitalModel
    capitais: list[CapitalModel] = []
    for capital_dict in data:
        for name, attrs in capital_dict.items():
            attrs_copy = dict(attrs)
            attrs_copy.pop('neighbors', None)
            capitais.append(CapitalModel(neighbors=name, **attrs_copy))

    # Exemplo: printar os títulos
    print(f"Projeto rodando...")
    for capital in capitais:
        print(capital.neighbors)


def seed_graph():
    file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..", "data", "capitais.json")
    file_path = os.path.normpath(file_path)

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    graph = Graph()
    for capital_dict in data:
        for name, attrs in capital_dict.items():
            toll = attrs.get("toll", 0)
            neighbors = attrs.get("neighbors", {})
            graph.add_vertex(name, CapitalModel(toll=toll, neighbors=neighbors.copy()))
    return graph


if __name__ == "__main__":
    GraphConstructor()
