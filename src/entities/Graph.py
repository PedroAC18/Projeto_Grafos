class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.matriz_adj = [[0] * num_vertices for _ in range(num_vertices)]
        self.lista_adj = [[] for _ in range(num_vertices)]

    def adicionar_aresta(self, origem, destino, peso=1):
        self.matriz_adj[origem][destino] = peso
        self.lista_adj[origem].append((destino, peso))

    def remover_aresta(self, origem, destino):
        self.matriz_adj[origem][destino] = 0
        for i, (vertice, peso) in enumerate(self.lista_adj[origem]):
            if vertice == destino:
                del self.lista_adj[origem][i]
                break

    def ponderar_vertice(self, vertice, peso):
        self.lista_adj[vertice] = peso

    def rotular_vertice(self, vertice, rotulo):
        self.lista_adj[vertice] = rotulo

    def ponderar_aresta(self, origem, destino, peso):
        self.matriz_adj[origem][destino] = peso
        for i, (vertice, peso) in enumerate(self.lista_adj[origem]):
            if vertice == destino:
                self.lista_adj[origem][i] = (vertice, peso)
                break

    def rotular_aresta(self, origem, destino, rotulo):
        self.matriz_adj[origem][destino] = rotulo

    def verificar_adjacencia_vertice(self, vertice1, vertice2):
        return self.matriz_adj[vertice1][vertice2] != 0

    def verificar_adjacencia_aresta(self, origem, destino):
        for vertice, _ in self.lista_adj[origem]:
            if vertice == destino:
                return True
        return False

    def verificar_incidencia(self, origem, destino, vertice):
        if self.matriz_adj[origem][destino] != 0 and self.matriz_adj[origem][vertice] != 0:
            return True
        return False

    def verificar_existencia_aresta(self, origem, destino):
        return self.matriz_adj[origem][destino] != 0

    def verificar_quantidade_vertices(self):
        return self.num_vertices

    def verificar_quantidade_arestas(self):
        count = 0
        for linha in self.matriz_adj:
            for valor in linha:
                if valor != 0:
                    count += 1
        return count

    def verificar_grafo_vazio(self):
        for linha in self.matriz_adj:
            for valor in linha:
                if valor != 0:
                    return False
        return True

    def verificar_grafo_completo(self):
        for linha in self.matriz_adj:
            for valor in linha:
                if valor == 0:
                    return False
        return True

    def obter_matriz_adjacencia(self):
        """
        Retorna a representação do grafo utilizando a matriz de adjacência.

        Returns:
            list: Matriz de adjacência do grafo.

        Exemplo:
            matriz_adj = grafo.obter_matriz_adjacencia()
        """
        return self.matriz_adj

    def obter_lista_adjacencia(self):
        """
        Retorna a representação do grafo utilizando a lista de adjacência.

        Returns:
            list: Lista de adjacência do grafo.

        Exemplo:
            lista_adj = grafo.obter_lista_adjacencia()
        """
        return self.lista_adj
