def gerar_vizinhos(estado):
    movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # U, D, L, R
    vazio = encontrar_vazio(estado)
    for linha in estado:
        print(f"--------------------------- {linha}")
    vizinhos = []

    if vazio:
        for movimento in movimentos:
            novo_x, novo_y = vazio[0] + movimento[0], vazio[1] + movimento[1]
            if novo_x < 0 or novo_x > 2 or novo_y < 0 or novo_y > 2:
                continue
            if 0 <= novo_x < len(estado) and 0 <= novo_y < len(estado[0]):
                novo_estado = [list(linha) for linha in estado]
                novo_estado[vazio[0]][vazio[1]], novo_estado[novo_x][novo_y] = novo_estado[novo_x][novo_y], \
                novo_estado[vazio[0]][vazio[1]]
                vizinhos.append(novo_estado)

                for linha in novo_estado:
                    print(linha)

    return vizinhos

def encontrar_vazio(estado):
    for i, linha in enumerate(estado):
        for j, valor in enumerate(linha):
            if valor == " " or valor == '' or valor == 0 or valor is None:
                return (i, j)
    return None