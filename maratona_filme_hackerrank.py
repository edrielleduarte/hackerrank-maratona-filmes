def acharMinimoDeDias(duracoes):
    numero_dias = 0
    duracoes = sorted(duracoes)

    while duracoes:
        tempo_maior = duracoes.pop(-1)

        if len(duracoes) == 0:
            numero_dias += 1
            break
        elif tempo_maior > 1.99:
            numero_dias += 1
            continue

        diferenca = 3 - tempo_maior

        if diferenca in duracoes:
            numero_dias += 1
            duracoes.remove(diferenca)

        else:
            achou_filme = False
            for tempo in duracoes:
                if tempo + tempo_maior <= 3:
                    numero_dias += 1
                    duracoes.remove(tempo)
                    achou_filme = True
                    break

            if not achou_filme:
                numero_dias += 1

    return numero_dias


if __name__ == '__main__':
    lista_1 = [1.01, 1.991, 1.32, 1.4]
    lista_2 = [1.90, 1.04, 1.25, 2.5, 1.75]

    print(f'O minimo de dias é: {acharMinimoDeDias(lista_1)}')
    print(f'O minimo de dias é: {acharMinimoDeDias(lista_2)}')
