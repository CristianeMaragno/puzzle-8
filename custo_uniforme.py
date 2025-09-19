# apesar do algoritmo agir como uma busca cega, implementei para que 
# considerasse o custo do caminho, que é sempre 1 para cada movimento.
# FIFO
import time
from node import Node
from utils import gerar_vizinhos

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
