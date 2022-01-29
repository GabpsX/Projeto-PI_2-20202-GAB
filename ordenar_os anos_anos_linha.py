# esse arquivo nao sera importado, sendo somente para ordenar os dados.
import csv
#Desempenho do <País> no período que vai desde o <ano 1> até o <ano 2> em
#olimpíadas de <Tipo de Olimpíada>, três linhas, uma por cada tipo de medalha
#esse cogigo ordena os elementos da coluna ano, entao a partir disso foi possivel descobrir o ano 1 e o ano 2
# descobrindo quais são os ultimos anos
with open("dados_glinha.csv", 'r') as infile:
    reader = csv.reader(infile, delimiter=",")
    ano = []
    for row in reader:
        #ordenando e retirando elementos iguais da lista
        ano.append(row[0])
    print(sorted(set(ano)))