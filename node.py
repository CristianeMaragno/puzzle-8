

class Node:
    def __init__(self, estado, pai=None, custo=0, heuristica=0, caminho=[]):
        self.estado = estado
        self.pai = pai
        self.custo = custo
        self.heuristica = heuristica
        self.f = custo + heuristica
        self.caminho = list(caminho)

    def __lt__(self, other):
        return (self.custo + self.heuristica) < (other.custo + other.heuristica)

    def __eq__(self, other):
        return self.estado == other.estado
    
    def __hash__(self):
        return hash(tuple(map(tuple, self.estado)))
    # garante que o hash seja gerado a partir de uma estrutura imutável