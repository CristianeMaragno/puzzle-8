import time
from node import Node
from utils import gerar_vizinhos

total_visitados = 0
maior_abertos = 0
arquivo_saida = "resultado-heurística.txt"

def a_estrela(tabuleiro, heuristica, estado_final):
    resultado = heuristica(tabuleiro, estado_final)
    return resultado

def heuristica_admissivel_simples(tabuleiro, estado_final):
    print("\nHeuristica Admissível Simples Selecionado")

    inicio_do_tempo = time.time()

    global total_visitados, maior_abertos, arquivo_saida
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
            criar_arquivo_saida(visitados, abertos)
            return total_visitados, len(no_atual.caminho), tempo_total, maior_abertos, arquivo_saida, no_atual.caminho

        melhor_caminho = []
        mais_proximo_resposta = 100
        for estado, movimento in gerar_vizinhos(no_atual.estado):
            novo_caminho = no_atual.caminho + [movimento]
            vizinho = Node(estado, pai=no_atual, custo=no_atual.custo + 1, caminho=novo_caminho)

            if vizinho not in visitados and vizinho not in abertos:
                novo_valor = calcular_heuristica(vizinho)
                if novo_valor < mais_proximo_resposta:
                    mais_proximo_resposta = novo_valor
                    melhor_caminho = [vizinho]
                elif  novo_valor == mais_proximo_resposta:
                    melhor_caminho.append(vizinho)

            if len(abertos) > maior_abertos:
                maior_abertos = len(abertos)

        if len(melhor_caminho) > 0:
            for caminho in melhor_caminho:
                abertos.append(caminho)

    print("Nenhuma solução encontrada.")
    return None

def heuristica_nao_admissivel(tabuleiro, estado_final):
    print("\nHeuristica Não Admissível Selecionado")

    inicio_do_tempo = time.time()

    global total_visitados, maior_abertos, arquivo_saida
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
            criar_arquivo_saida(visitados, abertos)
            return total_visitados, len(no_atual.caminho), tempo_total, maior_abertos, arquivo_saida, no_atual.caminho

        melhor_caminho = []
        mais_proximo_resposta = 100
        for estado, movimento in gerar_vizinhos(no_atual.estado):
            novo_caminho = no_atual.caminho + [movimento]
            vizinho = Node(estado, pai=no_atual, custo=no_atual.custo + 1, caminho=novo_caminho)

            if vizinho not in visitados and vizinho not in abertos:
                novo_valor = calcular_heuristica_nao_admissivel(vizinho) # Multiplicando para ver efeito piorando o algorítmo
                if novo_valor < mais_proximo_resposta:
                    mais_proximo_resposta = novo_valor
                    melhor_caminho = [vizinho]
                elif novo_valor == mais_proximo_resposta:
                    melhor_caminho.append(vizinho)

            if len(abertos) > maior_abertos:
                maior_abertos = len(abertos)

        if len(melhor_caminho) > 0:
            for caminho in melhor_caminho:
                abertos.append(caminho)

    print("Nenhuma solução encontrada.")
    return None

def heuristica_admissivel_complexa(tabuleiro, estado_final):
    print("\nHeuristica Extra Selecionado")
    return heuristica_admissivel_simples(tabuleiro, estado_final)

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
            resultado = resultado + abs((i - coordenadas_final[0])) + abs((j - coordenadas_final[1]))
    return resultado

def calcular_heuristica_nao_admissivel(nodo):
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
            resultado = resultado + abs((i - coordenadas_final[0])) * abs((j - coordenadas_final[1]))
    return resultado

def criar_arquivo_saida(visitados, abertos):
    with open(arquivo_saida, "w") as f:
        f.write("################################## ESTADOS VISITADOS ##################################\n\n")
        for no in visitados:
            for linha in no.estado:
                f.write(f"{linha}\n")
            f.write("\n")

        f.write("\n################################## ESTADOS ABERTOS ##################################\n\n")
        for no in abertos:
            for linha in no.estado:
                f.write(f"{linha}\n")
            f.write("\n")
