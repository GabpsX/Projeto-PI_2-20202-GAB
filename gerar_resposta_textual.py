# importando o biblioteca csv
import csv

###############################################
#Funcionamento do codigo
#Resposta Textual
#Quantas mulheres participaram da Olimpíada de <Cidade>?
#é perguntado a cidade entao, é contado o numero de mulheres que participaram da olimpiada da cidade desejada

################################################
# função resposta textual
def reposta_text():
    # entrada de valores
    entrada = input('Escolha a Cidade - Exemplo: Antwerpen: ')

    lista = []
    # abrindo arquivo csv
    with open('dados_resposta.csv') as csvfile:
        # leitura, delimitando espaço
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            # sexo == linha 0 do csv
            Sex = row[0]
            # se a linha 1 for igual a entrada use (dataframe-append) Sex linha = 0
            if row[1] == entrada:
                lista.append(Sex)
        # imprimir imformações

        print('A cidade desejada foi: {}'.format(entrada))
        print('Número de mulheres que participaram da olimpiada:', lista.count('F'))
        print('Número de homens que participaram da olimpiada:', lista.count('M'))
#######################################################################################
        total_de_mulheres = lista.count('F')
        total_de_homens = lista.count('M')
        somando = total_de_mulheres + total_de_homens
        print('O número total de pessoas que participaram foi de: {}'.format(somando))



# Resposta Textual - completo.
