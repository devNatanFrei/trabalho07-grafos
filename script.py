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

    def get_path(self, predecessors, start_vertex, end_vertex):
        path = []
        current = end_vertex
        while current is not None:
            path.insert(0, current)
            current = predecessors[current]
        if path[0] != start_vertex:  
            return None
        return ' -> '.join(path)



g = Grafo('grafo02.txt')
initial_vertex = input('Digite o vértice inicial: ').strip()
negative_cycle, distances, predecessors = g.bellman_ford(initial_vertex)

if not negative_cycle:
    print("\nResultados:")
    for vertex in g.grafo:
        if distances[vertex] != float('inf'):
            path = g.get_path(predecessors, initial_vertex, vertex)
            if initial_vertex != vertex:    
                print(f"Caminho de {initial_vertex} para {vertex}: {path}, Distância: {distances[vertex]}")
        else:
            print(f"Não há caminho de {initial_vertex} para {vertex}, Distância: Infinita")
else:
    print("Ciclo de peso negativo detectado! Não é possível calcular os caminhos mais curtos.")

    