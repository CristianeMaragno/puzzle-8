import time
from node import Node
from utils import gerar_vizinhos

total_visitados = 0 
maior_abertos = 0
arquivo_saida = "resultado-Custo-Uniforme.txt"

def custo_uniforme(tabuleiro, estado_final, texto):
    print(f"\nAlgoritmo {texto} selecionado")

    inicio_do_tempo = time.time()
    global total_visitados, maior_abertos, arquivo_saida

    no_inicial = Node(estado=tabuleiro, custo=0)
    
    abertos = [no_inicial]
    abertos_dict = {tuple(map(tuple, no_inicial.estado)): no_inicial}
    visitados = set()

    while abertos:
        abertos.sort(key=lambda no: no.custo)

        no_atual = abertos.pop(0)
        
        del abertos_dict[tuple(map(tuple, no_atual.estado))]
        
        visitados.add(tuple(map(tuple, no_atual.estado)))
        total_visitados += 1

        if no_atual.estado == estado_final.estado:
            fim_do_tempo = time.time()
            tempo_total = fim_do_tempo - inicio_do_tempo

            print("\nSolução encontrada!")
            criar_arquivo_saida(visitados, abertos)

            return total_visitados, len(no_atual.caminho), tempo_total, maior_abertos, arquivo_saida, no_atual.caminho

        for estado, movimento in gerar_vizinhos(no_atual.estado):
            vizinho_estado_tuple = tuple(map(tuple, estado))

            if vizinho_estado_tuple in visitados:
                continue

            novo_custo = no_atual.custo + 1
            
            if vizinho_estado_tuple in abertos_dict:
                no_existente = abertos_dict[vizinho_estado_tuple]
                if novo_custo < no_existente.custo:
                    abertos.remove(no_existente)
                    
                    novo_vizinho = Node(estado, pai=no_atual, custo=novo_custo, caminho=no_atual.caminho + [movimento])
                    
                    abertos.append(novo_vizinho)
                    abertos_dict[vizinho_estado_tuple] = novo_vizinho
            else:
                novo_vizinho = Node(estado, pai=no_atual, custo=novo_custo, caminho=no_atual.caminho + [movimento])
                abertos.append(novo_vizinho)
                abertos_dict[vizinho_estado_tuple] = novo_vizinho

        if len(abertos) > maior_abertos:
            maior_abertos = len(abertos)

    print("\nNenhuma solução encontrada.")
    return None

def criar_arquivo_saida(visitados, abertos):
    with open(arquivo_saida, "w") as f:
        f.write("################################### CUSTO UNIFORME ###################################\n\n")
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