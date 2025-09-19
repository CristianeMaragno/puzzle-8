import time
from node import Node
from utils import gerar_vizinhos

inicio_do_tempo = time.time()
total_visitados = 0
maior_abertos = 0
tamanho_caminho = 0
tempo_total = 0
arquivo_saida = "resultado.txt"

def a_estrela(tabuleiro, heuristica, estado_final):
    resultado = heuristica(tabuleiro, estado_final)
    return total_visitados, tamanho_caminho, tempo_total, maior_abertos, arquivo_saida

def heuristica_admissivel_simples(tabuleiro, estado_final):
    print("\nHeuristica Admissível Simples Selecionado")

    global total_visitados, maior_abertos, tamanho_caminho, arquivo_saida, inicio_do_tempo

    no_inicial = Node(estado=tabuleiro)
    abertos = [no_inicial]
    visitados = set()

    while abertos:
        no_atual = abertos.pop(0)
        visitados.add(no_atual)

        total_visitados += 1

        if no_atual.estado == estado_final.estado:
            fim_do_tempo = time.time()
            tempo_total = fim_do_tempo - inicio_do_tempo
            print("Solução encontrada!")
            return total_visitados, tamanho_caminho, tempo_total, maior_abertos, arquivo_saida

        melhor_caminho = None
        for vizinho_estado in gerar_vizinhos(no_atual.estado):
            vizinho = Node(vizinho_estado, pai=no_atual, custo= 1)

            if vizinho not in visitados and vizinho not in abertos:
                melhor_caminho = vizinho
                mais_proximo_resposta = 0
                novo_valor = calcular_heuristica(vizinho)
                if novo_valor >= mais_proximo_resposta:
                    mais_proximo_resposta = novo_valor
                    melhor_caminho = vizinho
            else:
                print("Estado já visitado ou na lista de abertos.")

        if melhor_caminho is not None:
            abertos.append(melhor_caminho)
        #abertos = []

    print("Nenhuma solução encontrada.")
    return None

def heuristica_nao_admissivel(tabuleiro, estado_final):
    print("\nHeuristica Não Admissível Selecionado")

    global total_visitados, maior_abertos, tamanho_caminho, arquivo_saida, inicio_do_tempo

    no_inicial = Node(estado=tabuleiro)
    abertos = [no_inicial]
    visitados = set()

    while abertos:
        no_atual = abertos.pop(0)
        visitados.add(no_atual)

        total_visitados += 1

        if no_atual.estado == estado_final.estado:
            fim_do_tempo = time.time()
            tempo_total = fim_do_tempo - inicio_do_tempo
            print("Solução encontrada!")
            return total_visitados, tamanho_caminho, tempo_total, maior_abertos, arquivo_saida

        melhor_caminho = None
        for vizinho_estado in gerar_vizinhos(no_atual.estado):
            vizinho = Node(vizinho_estado, pai=no_atual, custo=1)

            if vizinho not in visitados and vizinho not in abertos:
                melhor_caminho = vizinho
                mais_proximo_resposta = 0
                novo_valor = 2 * calcular_heuristica(vizinho) #Aplicando multiplicação para se tornar não admissível
                if novo_valor >= mais_proximo_resposta:
                    mais_proximo_resposta = novo_valor
                    melhor_caminho = vizinho
            else:
                print("Estado já visitado ou na lista de abertos.")

        if melhor_caminho is not None:
            abertos.append(melhor_caminho)
        # abertos = []

    print("Nenhuma solução encontrada.")
    return None

def heuristica_admissivel_complexa(tabuleiro, estado_final):
    print("\nHeuristica Extra Selecionado")
    pass

def calcular_heuristica(nodo):
    coordenadas_finais = {
        "1": (0, 0),
        "2": (0, 1),
        "3": (0, 2),
        "4": (1, 0),
        "5": (1, 1),
        "6": (1, 2),
        "7": (2, 0),
        "8": (2, 1),
        " ": (2, 2),
    }

    resultado = 0
    for i in range(len(nodo.estado)):  #percorre as linhas
        for j in range(len(nodo.estado[i])):  #percorre as colunas
            valor = nodo.estado[i][j]
            coordenadas_final = coordenadas_finais[valor]
            print(f"Valor: {valor} | Coordenadas atuais: ({i}, {j}) | Coordenadas finais: ({coordenadas_finais[valor]})")
            #print((i - coordenadas_final[0]))
            #print((j - coordenadas_final[1]))
            resultado = resultado + (i - coordenadas_final[0]) + (j - coordenadas_final[1])
            #print(resultado)
    print(f"Soma: {resultado}")
    return resultado
