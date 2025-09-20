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