import heapq

def dijkstra(graph, origem, destino, preco_combustivel, autonomia):
    # graph: instancia de Graph
    # origem, destino: nomes das capitais
    # preco_combustivel: float
    # autonomia: float

    dist = {v: float('inf') for v in graph.vertices}
    prev = {v: None for v in graph.vertices}
    dist[origem] = 0

    heap = [(0, origem)]  # (custo acumulado, capital atual)

    while heap:
        custo_atual, atual = heapq.heappop(heap)
        if atual == destino:
            break
        for vizinho, distancia in graph.vertices[atual].neighbors.items():
            # Custo combustível
            custo_combustivel = (distancia / autonomia) * preco_combustivel
            # Custo pedágio do vizinho
            custo_pedagio = graph.vertices[vizinho].toll
            custo_total = custo_combustivel + custo_pedagio
            novo_custo = custo_atual + custo_total
            if novo_custo < dist[vizinho]:
                dist[vizinho] = novo_custo
                prev[vizinho] = atual
                heapq.heappush(heap, (novo_custo, vizinho))

    # Reconstruir caminho
    caminho = []
    atual = destino
    while atual:
        caminho.append(atual)
        atual = prev[atual]
    caminho.reverse()
    return caminho, dist[destino]