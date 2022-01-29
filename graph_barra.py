import csv
import matplotlib.pyplot as plt
def apresentar_graficobarra():
#ultimos anos  '2010', '2012', '2014', '2016'
    esportes = input(
        'Escolha o esporte - Exemplo: Basketball: '
    )
    #anos selecionados

    ano = input('Escolha o ano: Ex: 1896: ')

    # entrada de valores

    season = input(
        'Escolha o tipo de olimpiada - Exemplo: Summer: '
    )

    lista_mulher = []
    lista_homem = []

    # abrindo arquivo csv
    with open('dados_gbarra.csv') as csvfile:
        # leitura, delimitando espaço
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            altura = row[0]
            if row[3] == esportes and row[4] == ano and row[2] == season and row[1] == 'F' and 'NA' not in row[0]:
                lista_mulher.append(altura)
            if row[3] == esportes and row[4] == ano and row[2] == season and row[1] == 'M' and 'NA' not in row[0]:
                lista_homem.append(altura)
    #tratando os dados

    new_mulheres = [float(val) for val in lista_mulher]
    new_homens = [float(val) for val in lista_homem]


    media = sum(new_mulheres) / len(new_mulheres)
    media2 = sum(new_homens) / len(new_homens)
    #plotando o grafico
    x = ['Mulheres', 'Homens']
    y = [media, media2]
    
    plt.figure(figsize=(10, 6))
    plt.bar(x, y, color = 'blue')
    plt.xticks(x)
    plt.ylabel('Valores de Media')
    plt.xlabel('Sexo')
    plt.title('Media de altura entre Mulheres e Homens do esporte {}'.format(esportes))
    # salva a figura do grafico ===     'nome do arquivo' . <== dot e formato de extensao ==   eps, jpeg, jpg, pdf, pgf, png, ps, raw, rgba, svg, svgz, tif, tiff
    plt.savefig('Grafico_de_barra.png')
    #plt.close() #para nao exibir o grafico e somente salvar
    print('O seu gráfico foi salvo - Grafico_de_barra.png')
    plt.show()

