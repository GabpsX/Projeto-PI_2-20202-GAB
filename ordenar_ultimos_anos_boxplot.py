# esse arquivo nao sera importado, sendo somente para ordenar os dados.
import csv
# descobrindo quais são os ultimos anos
#X18. IMC dos atletas do <Evento> nas últimas <X> olimpíadas de <Tipo de Olimpíada>
#esse cogido ordena a linha ano e renorna os valores na ordem, entao assim e possivel descobrir as ultimas x olimpiadas
with open("dados_boxplot.csv", 'r') as infile:
    reader = csv.reader(infile, delimiter=",")
    ano = []
    for row in reader:
        #ordenando e retirando elementos iguais da lista
        ano.append(row[0])
    print(sorted(set(ano)))