from custo_uniforme import custo_uniforme
from a_estrela import a_estrela, heuristica_nao_admissivel, heuristica_admissivel_simples, heuristica_admissivel_complexa 
from node import Node

estado_final = Node(estado=[["1", "2", "3"],
                ["4", "5", "6"],    
                ["7", "8", " "]], custo=0)

def estado_inicial(caminho):
    tabuleiro = []
    try: 
        with open(caminho, "r", encoding="utf-8") as file:
            for linha in file:
                linha = linha.strip()
                if linha:
                    elementos = [e.strip().strip('"') for e in linha.split(',')]
                    tabuleiro.append(elementos)

    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")

    return tabuleiro

def menu(tabuleiro):
    
    algoritmos = {
        1: (custo_uniforme, None),
        2: (a_estrela, heuristica_nao_admissivel),
        3: (a_estrela, heuristica_admissivel_simples),
        4: (a_estrela, heuristica_admissivel_complexa)
    }
    while True:
        try:
            escolha = int(input("\nEscolha um algoritmo: \n"
                                "1 - Custo Uniforme\n"
                                "2 - A* Heuristica Não Admissivel\n"
                                "3 - A* Heuristica Admissivel Simples\n"
                                "4 - A* Heuristica Admissivel Complexa\n"))
            
            if escolha in algoritmos:
                algoritmo, heuristica = algoritmos[escolha]
                if heuristica:
                    resultado = algoritmo(tabuleiro, heuristica, estado_final)
                else:
                    resultado = algoritmo(tabuleiro, estado_final)

                if resultado is not None:
                    total_visitados, tamanho_caminho, tempo_total, maior_abertos, arquivo_saida = resultado
                    print("Total de nós visitados:", total_visitados)
                    print("Tamanho do caminho:", tamanho_caminho)
                    print("Tempo total:", tempo_total)
                    print("Maior quantidade de abertos:", maior_abertos)
                    print("Arquivo de saída:", arquivo_saida)
                else:
                    print("Nenhuma solução encontrada.")
                
                break
            else:
                print("Opção inválida. Por favor, escolha um número entre 1 e 4.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

def main():
    caminho = "tabuleiro.txt"
    tabuleiro = estado_inicial(caminho)

    if tabuleiro:
        menu(tabuleiro)
    else:
        print("Tabuleiro inicial não pôde ser carregado.")


if __name__ == "__main__":
    main()
    