

class Node:
    def __init__(self, estado, pai=None, custo=0, valor_heuristica=0, caminho=[]):
        self.estado = estado
        self.pai = pai
        self.custo = custo
        self.valor_heuristica = valor_heuristica
        self.f = custo + valor_heuristica
        self.caminho = list(caminho) # impede que o caminho original seja modificado

    def __lt__(self, other):
        return self.f < other.f

    def __eq__(self, other):
        return self.estado == other.estado
    
    def __hash__(self):
        return hash(tuple(map(tuple, self.estado)))
    # garante que o hash seja gerado a partir de uma estrutura imutável