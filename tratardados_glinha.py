import csv
#salva um arquivo com os dados que serao utilizados para plotar o grafico
def tratar_dados_linha():
    outfile = open('dados_glinha.csv', 'w')
    outfile_csv = "year,medals,season,nacionalidade\n"
    outfile.write(outfile_csv)
    with open("athlete_events.csv", 'r') as infile:
        reader = csv.reader(infile, delimiter=",")
        header = next(reader)
        #print(header)
        #9 year
        #14 medal
        for row in reader:
            ano = row[9]
            medalhas = row[14]
            season = row[10]
            nacionalidade = row[6]
            #print(ano, medalhas)
            new = '{},{},{},{}\n'.format(ano,medalhas,season,nacionalidade)
            outfile.write(new)

