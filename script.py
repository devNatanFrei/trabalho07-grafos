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
                    if distances[u] != float('inf') and distances[u] + self.grafo[u][v] < distances[v]:
                        distances[v] = distances[u] + self.grafo[u][v]
                        predecessors[v] = u

        
        negative_edges = set()
        for u in self.grafo:
            for v in self.grafo[u]:
                if distances[u] != float('inf') and distances[u] + self.grafo[u][v] < distances[v]:
                    negative_edges.add((u, v))

        return distances, predecessors, negative_edges

    def remove_vertices(self, vertices_to_remove):
        for v in vertices_to_remove:
            if v in self.grafo:
                del self.grafo[v]
            for u in self.grafo:
                if v in self.grafo[u]:
                    del self.grafo[u][v]

    def reconstruct_path(self, start_vertex, end_vertex, predecessors):
        path = []
        current = end_vertex
        while current is not None and current != start_vertex:
            path.append(current)
            current = predecessors[current]
        if current == start_vertex:
            path.append(start_vertex)
        return path[::-1]

    def print_results(self, start_vertex, distances, predecessors, negative_edges):
        for end_vertex in self.grafo:
            if end_vertex == start_vertex:
                continue
            elif distances[end_vertex] == float('inf') or (end_vertex in negative_edges):
        
                if (start_vertex, end_vertex) in negative_edges or (end_vertex, start_vertex) in negative_edges:
                    print(f"Distância de {start_vertex} para {end_vertex} é: Infinita")
                else:
                    print(f"Distância de {start_vertex} para {end_vertex} é: Infinita")
            else:
                path = self.reconstruct_path(start_vertex, end_vertex, predecessors)
                print(f"Distância de {start_vertex} para {end_vertex} é: {distances[end_vertex]}")
                print(f"Caminho: {' -> '.join(path)}")

    def bellman_ford_ignore_cycles(self, start_vertex, negative_edges):
        distances = {v: float('inf') for v in self.grafo}
        predecessors = {v: None for v in self.grafo}
        distances[start_vertex] = 0


        for _ in range(len(self.grafo) - 1):
            for u in self.grafo:
                for v in self.grafo[u]:
                    if (u, v) in negative_edges or (v, u) in negative_edges:
                        continue  
                    if distances[u] != float('inf') and distances[u] + self.grafo[u][v] < distances[v]:
                        distances[v] = distances[u] + self.grafo[u][v]
                        predecessors[v] = u

        return distances, predecessors



g = Grafo('grafo01.txt')


initial_vertex = input('Digite o vértice inicial: ')


distances, predecessors, negative_edges = g.bellman_ford(initial_vertex)


distances, predecessors = g.bellman_ford_ignore_cycles(initial_vertex, negative_edges)


g.print_results(initial_vertex, distances, predecessors, negative_edges)
