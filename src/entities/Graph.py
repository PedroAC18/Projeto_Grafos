import copy

from src.entities.Aresta import Aresta
from src.entities.Vertice import Vertice


class Graph:
    def __init__(self, direcionado=True):
        self.lista_Vertices = []
        self.lista_Arestas = []
        self.direcionado = direcionado

    def novo_Vertice(self, identificador):
        self.lista_Vertices.append(Vertice(identificador))

    def nova_Aresta(self, origem, destino, peso):  # Método recebe dois identificadores
        origem_aux = self.busca_Vertice(origem)
        destino_aux = self.busca_Vertice(destino)
        if (origem_aux is not None) and (destino_aux is not None):
            self.lista_Arestas.append(Aresta(origem_aux, destino_aux, peso))
        else:
            print("Um do Vertice ou ambos são invalidos")

        if self.direcionado == False:
            self.lista_Arestas.append(Aresta(destino_aux, origem_aux, peso))  # Aresta(u,v) e Aresta(v,u)

    def busca_Aresta(self, u, v):  # Método recebe dois objetos do tipo Vértice
        for w in self.lista_Arestas:
            origem = w.getOrigem()
            destino = w.getDestino()
            if origem.getId() == u.getId() and destino.getId() == v.getId():
                return w

    def busca_Vertice(self, identificador):  # Método recebe um int
        for i in self.lista_Vertices:
            if identificador == i.getId():
                return i
        else:
            return None

    def esta_Vazio(self):
        if len(self.lista_Vertices) == 0:
            return True
        else:
            return False


    def copy(self):#faz uma copia do grafo para ser usado como auxiliar
        novoGrafo = copy.deepcopy(self)
        return novoGrafo
    def remove_Vertice(self, v : int):
        removido = self.copy()
        removido.lista_Vertices[v] = []
        for vertice in removido.lista_Vertices:
            while v in vertice:
                vertice.remove(v)
        return removido

    def busca_Adjacente(self, u):  # Método recebe um vertice
        for i in range(len(self.lista_Arestas)):
            origem = self.lista_Arestas[i].getOrigem()
            destino = self.lista_Arestas[i].getDestino()
            if (u.getId() == origem.getId()) and (destino.getVisitado() == False):
                destino.setVisitado(True)  # Para que não retorn o mesmo vertice seguidas veses
                return destino
        else:
            return None


    def busca_predecessor(self, n:int):
        predecessores = []
        for vertex in self.lista_Vertices:
            for aux in vertex:
                if aux == n:
                    predecessores.append(self.lista_Vertices.index(vertex))

        return predecessores

