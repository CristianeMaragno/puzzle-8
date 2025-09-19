# apesar do algoritmo agir como uma busca cega, implementei para que 
# considerasse o custo do caminho, que é sempre 1 para cada movimento.
# FIFO
import time
from node import Node

inicio_do_tempo = time.time()
total_visitados = 0 
maior_abertos = 0
tamanho_caminho = 0
arquivo_saida = "resultado.txt"

def custo_uniforme(tabuleiro, estado_final):
    print("\nCusto Uniforme selecionado")

    global total_visitados, maior_abertos, tamanho_caminho, arquivo_saida, inicio_do_tempo

    no_inicial = Node(estado=tabuleiro, custo=0)
    
    abertos = [no_inicial]
    visitados = set()

    while abertos:
        abertos.sort(key=lambda Node: Node.custo)

        no_atual = abertos.pop(0)
        visitados.add(no_atual)

        total_visitados += 1

        if no_atual.estado == estado_final.estado:
            fim_do_tempo = time.time()
            tempo_total = fim_do_tempo - inicio_do_tempo
            print("Solução encontrada!")
            return total_visitados, tamanho_caminho, tempo_total, maior_abertos, arquivo_saida

        for vizinho_estado in gerar_vizinhos(no_atual.estado):
            vizinho = Node(vizinho_estado, pai=no_atual, custo= 1)

            if vizinho not in visitados and vizinho not in abertos:
                abertos.append(vizinho)
                if len(abertos) > maior_abertos:
                    maior_abertos = len(abertos)
            else:
                print("Estado já visitado ou na lista de abertos.")

    print("Nenhuma solução encontrada.")
    return None

def gerar_vizinhos(estado):
    movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # U, D, L, R
    vazio = encontrar_vazio(estado)
    for linha in estado:
        print(f"--------------------------- {linha}")
    vizinhos = []
    
    if vazio:
        for movimento in movimentos:
            novo_x, novo_y = vazio[0] + movimento[0], vazio[1] + movimento[1]
            if novo_x < 0 or novo_x > 2 or novo_y < 0 or novo_y > 2:
                continue
            print(novo_x, novo_y)
            if 0 <= novo_x < len(estado) and 0 <= novo_y < len(estado[0]):
                novo_estado = [list(linha) for linha in estado]
                novo_estado[vazio[0]][vazio[1]], novo_estado[novo_x][novo_y] = novo_estado[novo_x][novo_y], novo_estado[vazio[0]][vazio[1]]
                vizinhos.append(novo_estado)

                for linha in novo_estado:
                    print(linha)

    return vizinhos

def encontrar_vazio(estado):
    for i, linha in enumerate(estado):
        for j, valor in enumerate(linha):
            if valor == " " or valor == '' or valor == 0 or valor is None:
                return (i, j)
    return None
