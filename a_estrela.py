import time
from node import Node
from utils import gerar_vizinhos

total_visitados = 0
maior_abertos = 0
arquivo_saida = "resultado-heurística.txt"

def a_estrela(tabuleiro, heuristica, estado_final, texto): #f(n) = g(n) + h(n)
    print(f"\nAlgoritmo A* {texto} selecionado")
    inicio_do_tempo = time.time()

    global total_visitados, maior_abertos, arquivo_saida
    
    no_inicial = Node(estado=tabuleiro, custo=0)
    no_inicial.valor_heuristica = heuristica(no_inicial)
    no_inicial.f = no_inicial.custo + no_inicial.valor_heuristica

    abertos = [no_inicial]
    abertos_dict = {tuple(map(tuple, no_inicial.estado)): no_inicial}
    visitados = set()

    while abertos:
        abertos.sort(key=lambda no: no.f)
        
        no_atual = abertos.pop(0)
        
        del abertos_dict[tuple(map(tuple, no_atual.estado))]
        
        
        visitados.add(tuple(map(tuple, no_atual.estado)))
        total_visitados += 1
        
        if no_atual.estado == estado_final.estado:
            fim_do_tempo = time.time()
            tempo_total = fim_do_tempo - inicio_do_tempo
            print("Solução encontrada!")
            criar_arquivo_saida(visitados, abertos)
            return total_visitados, len(no_atual.caminho), tempo_total, maior_abertos, arquivo_saida, no_atual.caminho

      
        for estado, movimento in gerar_vizinhos(no_atual.estado):
            vizinho_estado_tuple = tuple(map(tuple, estado))

           
            if vizinho_estado_tuple in visitados:
                continue

            novo_custo = no_atual.custo + 1
            
            if vizinho_estado_tuple in abertos_dict:
                no_existente = abertos_dict[vizinho_estado_tuple]
                novo_vizinho_f = novo_custo + heuristica(Node(estado))
                
                if novo_vizinho_f < no_existente.f:
                    abertos.remove(no_existente)
                    
                    novo_vizinho = Node(estado, pai=no_atual, custo=novo_custo, caminho=no_atual.caminho + [movimento])
                    novo_vizinho.valor_heuristica = heuristica(novo_vizinho)
                    novo_vizinho.f = novo_vizinho.custo + novo_vizinho.valor_heuristica
                    
                    abertos.append(novo_vizinho)
                    abertos_dict[vizinho_estado_tuple] = novo_vizinho
            else:
                novo_vizinho = Node(estado, pai=no_atual, custo=novo_custo, caminho=no_atual.caminho + [movimento])
                novo_vizinho.valor_heuristica = heuristica(novo_vizinho)
                novo_vizinho.f = novo_vizinho.custo + novo_vizinho.valor_heuristica
                abertos.append(novo_vizinho)
                abertos_dict[vizinho_estado_tuple] = novo_vizinho
            
        if len(abertos) > maior_abertos:
            maior_abertos = len(abertos)

    print("\nNenhuma solução encontrada.")
    return None
    
def heuristica_nao_admissivel(nodo): #superestimar o custo
    return calcular_heuristica_nao_admissivel(nodo)

def heuristica_admissivel_simples(nodo):
    return calcular_heuristica_distancia(nodo)

def heuristica_admissivel_complexa(nodo):
    return calcular_heuristica_admissivel_complexa(nodo)


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

def calcular_heuristica_distancia(nodo):
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

def calcular_heuristica_valores_fora(nodo):
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
    for i in range(len(nodo.estado)):  # percorre as linhas
        for j in range(len(nodo.estado[i])):  # percorre as colunas
            valor = nodo.estado[i][j]
            coordenadas_final = coordenadas_finais[valor]
            if (i is not coordenadas_final[0]) or (j is not coordenadas_final[1]):
                resultado = resultado + 1
    return resultado

def calcular_heuristica_admissivel_complexa(nodo):
    calculo_distancia = calcular_heuristica_distancia(nodo)
    calculo_fora_lugar = calcular_heuristica_valores_fora(nodo)
    return max(calculo_distancia, calculo_fora_lugar)

def criar_arquivo_saida(visitados, abertos):
    with open(arquivo_saida, "w") as f:
        f.write("#################################### A* HEURISTICA ####################################\n\n")
        f.write("################################## ESTADOS VISITADOS ##################################\n\n")
        for estado_tuple in visitados:
            for linha_tuple in estado_tuple:
                f.write(f"{list(linha_tuple)}\n")
            f.write("\n")

        f.write("\n################################## ESTADOS ABERTOS ##################################\n\n")
        for no in abertos:
            for linha in no.estado:
                f.write(f"{linha}\n")
            f.write("\n")