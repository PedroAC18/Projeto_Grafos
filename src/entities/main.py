from Graph import MyGraph
import sys
from datetime import datetime

sys.setrecursionlimit(200000000)
#Representação utilizando Matriz/Lista de Adjacência

g = MyGraph(full=5, n_vrt=5)
print(g.get_adjacency_matrix())
print(g.get_adjacency_list())
g.show()

# Criação de grafos com X vértices
g = MyGraph(n_vrt=5)

# Adição de arestas
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
# g.show()

# Remoção de Arestas
g.remove_edge(2, 3)
# g.show()

# Ponderação de vértices
g = MyGraph(n_vrt=4)
g.set_vertex_label(0, "Pedro")
g.set_vertex_label(1, "Luiz")
g.set_vertex_label(2, "Samuel")
g.set_vertex_label(3, "Victor")
g.show()

# Ponderação de arestas
g = MyGraph(n_vrt=3)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.set_edge_label(0, 1, "Teste")
g.set_edge_label(1, 2, "Teste2")
g.get_edge_label(1, 2)
g.set_edge_val(1, 2, 5)
g.set_edge_val(1, 2, 10)
g.show()

# Checagem de adjacência entre vértices
g = MyGraph(n_vrt=3)
g.add_edge(0, 1)
g.add_edge(1, 2)
print("Vértice 0 e 1 são adjacentes: ", g.is_vertices_adjacents(0, 1))
print("Vértice 2 e 0 são adjacentes: ", g.is_vertices_adjacents(2, 0))

# Checagem de adjacência entre arestas
g = MyGraph(n_vrt=4)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
print("Arestas são adjacentes: ", g.is_edges_adjacents(0, 1, 1, 2))
print("Arestas são adjacentes: ", g.is_edges_adjacents(0, 3, 2, 3))

# Checagem da existência de arestas
g = MyGraph(n_vrt=4)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
print("Existe aresta: ", g.edge_exists(0, 1))
print("Existe aresta: ", g.edge_exists(1, 3))

# Checagem de quantidade de vértices e arestas
g = MyGraph(n_vrt=5)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
print(g.vertex_count())
print(g.edges_count())

# Checagem de grafo vazio
g = MyGraph(n_vrt=5)
g.add_edge(0, 1)
print(g.is_graph_empty())
g.remove_edge(0, 1)
print(g.is_graph_empty())

# Checagem de grafo completo
g = MyGraph(n_vrt=5, full=True)
print(g.is_full_graph())
g.remove_edge(0, 1)
print(g.is_full_graph())
