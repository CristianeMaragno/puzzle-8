# apesar do algoritmo agir como uma busca cega, implementei para que 
# considerasse o custo do caminho, que é sempre 1 para cada movimento.
# FIFO
import time
from node import Node

total_visitados = 0 
maior_abertos = 0
arquivo_saida = "resultado-Custo-Uniforme.txt"

def custo_uniforme(tabuleiro, estado_final):
    print("\nCusto Uniforme selecionado")

    inicio_do_tempo = time.time()
    global total_visitados, maior_abertos, arquivo_saida

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

            print("\nSolução encontrada!")
            criar_arquivo_saida(visitados, abertos)

            return total_visitados, len(no_atual.caminho), tempo_total, maior_abertos, arquivo_saida, no_atual.caminho

        for estado, movimento in gerar_vizinhos(no_atual.estado):

            novo_caminho = no_atual.caminho + [movimento]
            vizinho = Node(estado, pai=no_atual, custo=no_atual.custo+1, caminho=novo_caminho)


            if vizinho in visitados:
                continue

            no_igual = None
            for no in abertos:
                if no.estado == vizinho.estado:
                    no_igual = no
                    break
            if no_igual:
                if vizinho.custo < no_igual.custo:
                    abertos.remove(no_igual)
                    abertos.append(vizinho)
            else:
                abertos.append(vizinho)

            if len(abertos) > maior_abertos:
                maior_abertos = len(abertos)

    print("\nNenhuma solução encontrada.")
    return None

def gerar_vizinhos(estado):
    movimentos = {
        'U': (-1, 0),
        'D': (1, 0),
        'L': (0, -1),
        'R': (0, 1)
    }
    vazio = encontrar_vazio(estado)
    vizinhos = []

    if vazio:
        for direcao, (dx, dy) in movimentos.items():
            novo_x, novo_y = vazio[0] + dx, vazio[1] + dy

            if 0 <= novo_x < len(estado) and 0 <= novo_y < len(estado[0]):

                novo_estado = [list(linha) for linha in estado]

                novo_estado[vazio[0]][vazio[1]], novo_estado[novo_x][novo_y] = \
                    novo_estado[novo_x][novo_y], novo_estado[vazio[0]][vazio[1]]

                vizinhos.append((novo_estado, direcao))

    return vizinhos

def encontrar_vazio(estado):
    for i, linha in enumerate(estado):
        for j, valor in enumerate(linha):
            if valor == " " or valor == '' or valor == 0 or valor is None:
                return (i, j)
    return None

def criar_arquivo_saida(visitados, abertos):
    with open(arquivo_saida, "w") as f:
        f.write("################################### CUSTO UNIFORME ###################################\n\n")
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