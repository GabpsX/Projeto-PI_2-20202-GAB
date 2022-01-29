import csv

import matplotlib.pyplot as plt
#########################################################
#funcionamento do codigo:
#Gráfico de Linhas
#L5. Desempenho do <País> no período que vai desde o <ano 1> até o <ano 2> em
#olimpíadas de <Tipo de Olimpíada>, três linhas, uma por cada tipo de medalha

#primeiro é perguntado o pais, depois é perguntado o tipo de olimpiada, entao é escolhido todos os anos
#do intervalo do ano 1 até o  ano 2, depois é contado as medalhas e as mesmas são armazenadas em 3 listas uma para cada tipo
#que sera utilizada para plotar o grafico.
#como foram escolhidos os anos 1 e 2? = criei uma função que gera uma lista e ordena os do numero menor para o maior
#########################################################


# '1896', '1900', '1904' primeiros 3 anos
# ano 1 e ano 2 = '1896', '1900', e esporte
def desempenho_pais():
    pais = input(
        'Escolha o pais - Exemplo: China: '
    )
    # para caso queira mudar o intervalo de anos
    #choose = input('Escolha dois anos: Ex: 1896 1900: ')
    #ano1d1, ano2d2 = choose.split()
    ano1d1 = str(1896)
    ano2d2 = str(1900)
    # entrada de valores

    season = input(
        'Escolha o tipo de olimpiada: Exemplo: Summer: '
    )

    anos_escolhido1 = []
    anos_escolhido2 = []

    # abrindo arquivo csv
    with open('dados_glinha.csv') as csvfile:
        # leitura, delimitando espaço
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            medals = row[1]
            if row[0] >= ano1d1 and row[2] == season and row[3] == pais:
                anos_escolhido1.append(medals)
            if row[0] <= ano2d2 and row[2] == season and row[3] == pais:
                anos_escolhido2.append(medals)


        # contando o numero de medalhas por ano e esporte
        ##################################################
        ##################################################
        Gold_ano1 = anos_escolhido1.count('Gold')
        Silver_ano1 = anos_escolhido1.count('Silver')
        Bronze_ano1 = anos_escolhido1.count('Bronze')
        print(5 * '=-=')
        Gold_ano2 = anos_escolhido2.count('Gold')
        Silver_ano2 = anos_escolhido2.count('Silver')
        Bronze_ano2 = anos_escolhido2.count('Bronze')

        #################################################################################
        # plotando o grafico
        gold = [Gold_ano1, Gold_ano2]
        print('ouro = ', gold)

        silver = [Silver_ano1, Silver_ano2]
 
        bronze = [Bronze_ano1, Bronze_ano2]
 
        #x = 10 * np.array(range(len(gold)))
        #x label
        b = Gold_ano1, Gold_ano2
        var1 = " ".join(map(str,b))
        u, h = var1.split()

        x = u, h
        # primeira linha
        plt.figure(figsize=(10, 6))
        plt.plot(x, gold, 'go', color='g', label='gold')  # 'go' == bola
        plt.plot(x, gold, color='g')
        # segundo linha
        plt.plot(x, silver, 'r^', color='r', label='silver')  # 'r^'^== triangulo
        plt.plot(x, silver, color='r')
        # terceira linha
        plt.plot(x, bronze, 's', color='b', label='bronze')  # 's' == quadrado
        plt.plot(x, bronze)
        # titulo do grafico
        # plt.title("Medalhas das Olimpiadas dos anos: {} {} {} Season {}".format(ano, ano2, ano3 , season))
        plt.title("Medalhas das Olimpiadas dos anos: de {} a {} Season {}".format(ano1d1, ano2d2, season))
        # ativa uma rede == quadrados no grafico
        plt.grid(True)
        # label x
        # d = ano, ano2, ano3
        a = 'O pais selecionado foi'
        plt.xlabel('{} {}'.format(a, pais))
        # label y
        plt.ylabel("Numero de medalhas")
        # legenda do grafico
        plt.legend()
        # salva a figura do grafico ===     'nome do arquivo' . <== dot e formato de extensao ==   eps, jpeg, jpg, pdf, pgf, png, ps, raw, rgba, svg, svgz, tif, tiff
        plt.savefig('Grafico_de_linha.png')
        print('O seu gráfico foi salvo - Grafico_de_linha.png')
        # plt.close()  <=== retirar comentario e deletar plt.show() caso nao queira mostrar o grafico
        plt.show()



