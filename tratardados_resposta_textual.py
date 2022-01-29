import csv
#salva um arquivo com os dados que serao utilizados para plotar o grafico
def tratar_dados_resposta():
    fil = open("dados_resposta.csv", "w")
    outfile_csv = "Sex,City\n"
    fil.write(outfile_csv)
    with open("athlete_events.csv", "r") as file:
        reader = csv.reader(file, delimiter=",")
        header = next(reader)
        for row in reader:
            Sex = row[2]
            City = row[11]
            barra = '{},{}\n'.format(Sex,City)
            fil.write(barra)
