import csv
#salva um arquivo com os dados que serao utilizados para plotar o grafico
def tratar_dados_box_plot():
    outfile = open('dados_boxplot.csv', 'w')
    outfile_csv = "year,peso,altura,evento,season\n"
    outfile.write(outfile_csv)
    with open("athlete_events.csv", 'r') as infile:
        reader = csv.reader(infile, delimiter=",")
        header = next(reader)
        #print(header)
        #9 year
        #14 medal
        for row in reader:
            ano = row[9]
            imc = row[5]
            altura = row[4]
            evento = row[13]
            season = row[10]
            #print(ano, medalhas)
            new = '{},{},{},{},{}\n'.format(ano,imc,altura,evento,season)
            outfile.write(new)
tratar_dados_box_plot()
