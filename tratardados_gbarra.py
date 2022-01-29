import csv
#salva um arquivo com os dados que serao utilizados para plotar o grafico
def tratar_dados_barra():
    fil = open("dados_gbarra.csv", "w")
    outfile_csv = "altura,sexo,season,esportes,ano\n"
    fil.write(outfile_csv)
    with open("athlete_events.csv", "r") as file:
        reader = csv.reader(file, delimiter=",")
        header = next(reader)
        for row in reader:
            altura = row[4]
            sexo = row[2]
            season = row[10]
            esportes = row[12]
            ano = row[9]
            barra = '{},{},{},{},{}\n'.format(altura,sexo,season,esportes,ano)
            fil.write(barra)
tratar_dados_barra()