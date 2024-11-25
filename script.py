class Grafo:
    def __init__(self, arquivo):
        self.grafo = {}
        self.load_data(arquivo)

    def load_data(self, arquivo):
        with open(arquivo, 'r') as f:
            linhas = f.readlines()
            for linha in linhas:
                linha = linha.strip()
                if linha:
                    a, b, peso = linha.split()
                    peso = int(peso)
                    self.add_edge(a, b, peso)

    def add_edge(self, a, b, peso):
        if a not in self.grafo:
            self.grafo[a] = {}
        if b not in self.grafo:
            self.grafo[b] = {}
        self.grafo[a][b] = peso

    def bellman_ford(self, start_vertex):
        distances = {v: float('inf') for v in self.grafo}
        predecessors = {v: None for v in self.grafo}
        distances[start_vertex] = 0

        for _ in range(len(self.grafo) - 1):
            for u in self.grafo:
                for v in self.grafo[u]:
                    if distances[u] + self.grafo[u][v] < distances[v]:
                        distances[v] = distances[u] + self.grafo[u][v]
                        predecessors[v] = u
                        print(f"Relaxando aresta {u}->{v}, nova distância para {v}: {distances[v]}")

        for u in self.grafo:
            for v in self.grafo[u]:
                if distances[u] + self.grafo[u][v] < distances[v]:
                    print("Ciclo negativo detectado!")
                    return (True, None, None)

        return (False, distances, predecessors)

 



grafh = Grafo('grafo02.txt')

initial_vertex = input('Digite o vértice inicial: ').strip()
if initial_vertex not in grafh.grafo:
    print("Vértice inicial não encontrado no grafo.")
else:
    has_negative_cycle, distances, predecessors = grafh.bellman_ford(initial_vertex)
    if has_negative_cycle:
        print("O grafo contém ciclos negativos. Não é possível calcular distâncias confiáveis.")
    else:
        print(f"Distâncias a partir do vértice {initial_vertex}:")
        for vertex, distance in distances.items():
            if  initial_vertex != vertex:
                print(f"{initial_vertex} -> {vertex}: {distance}")
