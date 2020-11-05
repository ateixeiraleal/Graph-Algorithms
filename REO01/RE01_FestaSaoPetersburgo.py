entrada = open('entrada.txt', 'r')
saida = open('saida.txt', 'w')
while True:
    dados = entrada.readline()
    pessoas = int(dados[0])
    amizades = int(dados[2])
    qde_minima_amigos = int(dados[4])
    print('A quantidade de pessoas na comunidade é: {}.'.format(pessoas))
    print('O número de ralação de amizades é {}.'.format(amizades))
    print('A quantidade mínima de amizades é {}.'.format(qde_minima_amigos))

    # Construindo a matriz de amizades
    n = amizades

    if n >= 2:
        m = list()
        vai = list()

        # Matriz base com elemento "0"
        for i in range(n):
            m.append([])
            for j in range(n):
                m[i].append(0)

        # Inserindo as amizades
        for i in range(0, n):
            dados = entrada.readline()
            l = int(dados[0]) - 1
            c = int(dados[2]) - 1
            m[l][c] = 1
            m[c][l] = 1

        # Deletando as amizades que não irao à festa
        for i in range(0, n):
            count = 0
            for j in range(0, n):
                if m[i][j] == 1:
                    count += 1
            if count < 2:
                for x in range(0, n):
                    if m[i][x] == 1:
                        m[i][x] = 0
                        m[x][i] = 0

        # Definindo quem irá à festa
        for i in range(0, n):
            count = 0
            for j in range(0, n):
                if m[i][j] == 1:
                    count += 1
            if count >= qde_minima_amigos:
                vai.append(i + 1)

        # Exibindo a matriz formada
        T = len(str(m[n - 1][n - 1]))
        for i in range(n):
            for j in range(n):
                m[i][j] = str(m[i][j])
                while len(m[i][j]) < T:
                    m[i][j] = ' ' + m[i][j]
            M = ' '.join(m[i])
            print(M)

        if len(vai) != 0:
            sorted(vai)
            lista = " ".join(map(str, vai))
            print('Pessoas que irão à festa {}.'.format(lista))
            saida.write(lista)
        else:
            print('Pessoas que irão à festa {}'.format(0))
            saida.write(0)

entrada.close()
saida.close()
