from dataclasses import dataclass

@dataclass
class CapitalModel:
    toll: int
    neighbors: dict  # {nome_vizinho: distancia}
