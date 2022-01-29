import csv
import matplotlib.pyplot as plt
#gera um grafico box plot
def apresentar_graficoboxplot():
    #X18. IMC dos atletas do <Evento> nas últimas <X> olimpíadas de <Tipo de <Olimpíada>
    
    Evento = input('Digite o evento: Ex: judo Mens Extra-Lightweight: ')
    #ano = input('Digite o ano: ')
    t_olimpiada = input('Digite o Tipo de Olimpíada: ')


    #ultimos x anos x = '2010', '2012', '2014', '2016'
    ano = str(2016)
    height = []
    weight = []
    #year0,peso1,altura2,evento3,season4
    with open('dados_boxplot.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            altura = row[2]
            peso = row[1]
            # se a linha 0 == ano e linha 3 == evento e se a linha 4 == tipo de olimpíada e se NA nao estiver na linha 1 e se NA  nao estuver na linha 2, juntar linha altura em uma lista, juntar linha peso em uma lista
            if row[0] == ano and row[3] == Evento and row[4] == t_olimpiada and 'NA' not in row[1] and 'NA' not in row[2]:
                height.append(altura)
                weight.append(peso)

    #transforma os valores em inteiros
    nheight = [int(val) for val in height]
    nweight = [int(val) for val in weight]

    #soma a lista
    somar = sum(nheight)
    somar2 = sum(nweight)
    #plotando o grafico

    #formula IMC = Peso ÷ (Altura × Altura)
    IMC = somar2 / (somar * somar)
    #axis x
    x=[0,IMC]
 
    plt.boxplot(x)
    #titulo
    plt.title("IMC")
    #salva uma figura do grafico
    plt.savefig('Grafico_de_barra.png')
    #mostra o grafico ou plota e fecha
    #plt.close() 
    plt.show()

