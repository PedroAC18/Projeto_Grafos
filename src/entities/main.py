from src.entities.Graph import Graph


def main():
    num_vertices = int(input("Digite o número de vértices do grafo: "))
    grafo = Graph(num_vertices)

    while True:
        print("==== MENU ====")
        print("1. Adicionar aresta")
        print("2. Remover aresta")
        print("3. Ponderar vértice")
        print("4. Rotular vértice")
        print("5. Rotular aresta")
        print("6. Verificar adjacência entre vértices")
        print("7. Verificar adjacência entre arestas")
        print("8. Verificar incidência entre aresta e vértices")
        print("9. Verificar existência de aresta")
        print("10. Verificar quantidade de vértices e arestas")
        print("11. Verificar se o grafo está vazio")
        print("12. Verificar se o grafo está completo")
        print("13. Representação do grafo utilizando Matriz de Adjacência")
        print("14. Representação do grafo utilizando Lista de Adjacência")
        print("0. Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            num_arestas = int(input("Digite o número de arestas a adicionar: "))
            for _ in range(num_arestas):
                origem = int(input("Digite o vértice de origem da aresta: "))
                destino = int(input("Digite o vértice de destino da aresta: "))
                grafo.adicionar_aresta(origem, destino)
            print("Arestas adicionadas com sucesso!")

        elif opcao == 2:
            origem = int(input("Digite o vértice de origem da aresta: "))
            destino = int(input("Digite o vértice de destino da aresta: "))
            grafo.remover_aresta(origem, destino)
            print("Aresta removida com sucesso!")

        elif opcao == 3:
            vertice = int(input("Digite o vértice a ser ponderado: "))
            peso = float(input("Digite o peso a ser atribuído ao vértice: "))
            grafo.ponderar_vertice(vertice, peso)
            print("Vértice ponderado com sucesso!")

        elif opcao == 4:
            vertice = int(input("Digite o vértice a ser rotulado: "))
            rotulo = input("Digite o rótulo a ser atribuído ao vértice: ")
            grafo.rotular_vertice(vertice, rotulo)
            print("Vértice rotulado com sucesso!")

        elif opcao == 5:
            origem = int(input("Digite o vértice de origem da aresta: "))
            destino = int(input("Digite o vértice de destino da aresta: "))
            rotulo = input("Digite o rótulo a ser atribuído à aresta: ")
            grafo.rotular_aresta(origem, destino, rotulo)
            print("Aresta rotulada com sucesso!")

        elif opcao == 6:
            vertice1 = int(input("Digite o primeiro vértice: "))
            vertice2 = int(input("Digite o segundo vértice: "))
            adjacencia = grafo.verificar_adjacencia_vertice(vertice1, vertice2)
            if adjacencia:
                print("Os vértices são adjacentes.")
            else:
                print("Os vértices não são adjacentes.")

        elif opcao == 7:
            origem = int(input("Digite o vértice de origem da aresta: "))
            destino = int(input("Digite o vértice de destino da aresta: "))
            adjacencia = grafo.verificar_adjacencia_aresta(origem, destino)
            if adjacencia:
                print("As arestas são adjacentes.")
            else:
                print("As arestas não são adjacentes.")

        elif opcao == 8:
            origem = int(input("Digite o vértice de origem da aresta: "))
            destino = int(input("Digite o vértice de destino da aresta: "))
            vertice = int(input("Digite o vértice a ser verificado: "))
            incidencia = grafo.verificar_incidencia(origem, destino, vertice)
            if incidencia:
                print("A aresta está incidindo no vértice.")
            else:
                print("A aresta não está incidindo no vértice.")

        elif opcao == 9:
            origem = int(input("Digite o vértice de origem da aresta: "))
            destino = int(input("Digite o vértice de destino da aresta: "))
            existencia = grafo.verificar_existencia_aresta(origem, destino)
            if existencia:
                print("A aresta existe no grafo.")
            else:
                print("A aresta não existe no grafo.")

        elif opcao == 10:
            num_vertices = grafo.verificar_quantidade_vertices()
            num_arestas = grafo.verificar_quantidade_arestas()
            print("Quantidade de vértices:", num_vertices)
            print("Quantidade de arestas:", num_arestas)

        elif opcao == 11:
            vazio = grafo.verificar_grafo_vazio()
            if vazio:
                print("O grafo está vazio.")
            else:
                print("O grafo não está vazio.")

        elif opcao == 12:
            completo = grafo.verificar_grafo_completo()
            if completo:
                print("O grafo está completo.")
            else:
                print("O grafo não está completo.")

        elif opcao == 13:
            matriz_adj = grafo.obter_matriz_adjacencia()
            print("Matriz de Adjacência:")
            for linha in matriz_adj:
                print(linha)

        elif opcao == 14:
            lista_adj = grafo.obter_lista_adjacencia()
            print("Lista de Adjacência:")
            for vertice, vizinhos in enumerate(lista_adj):
                print(f"Vértice {vertice}: {vizinhos}")
        elif opcao == 0:
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida. Por favor, tente novamente.")


if __name__ == '__main__':
    main()
