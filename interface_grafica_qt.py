from PyQt5 import QtWidgets, uic
from pathlib import Path

import graph_linha
import graph_barra
import graph_boxplot
import gerar_resposta_textual
#importando dados e funcoes:
import tratardados_glinha
import tratardados_gbarra
import tratardados_gboxplot
import tratardados_resposta_textual


#gerando arquivos

arquivo = Path("dados_glinha.csv")
arquivo1 = Path("dados_boxplot.csv")
arquivo2 = Path("dados_gbarra.csv")
arquivo3 = Path("dados_resposta.csv")
if (arquivo.is_file()) and (arquivo1.is_file()) and (arquivo2.is_file()) and (arquivo3.is_file()):
  print("Verificando arquivos!")
else:
  print("Tratando Dados!")
  tratardados_glinha.tratar_dados_linha()
  tratardados_gbarra.tratar_dados_barra()
  tratardados_gboxplot.tratar_dados_box_plot()
  tratardados_resposta_textual.tratar_dados_resposta()

class tela_inicio:
    def plot_gr(self):
        self.primeira_tela.ui.show()

    def plot_1(self):
         graph_linha.desempenho_pais()

    def plot_2(self):
         graph_barra.apresentar_graficobarra()
    
    def plot_3(self):
        graph_boxplot.apresentar_graficoboxplot()

    def textual(self):
        gerar_resposta_textual.reposta_text()

class execut(tela_inicio):

    def __init__(self):
        self.app = QtWidgets.QApplication([])

        self.primeira_tela = uic.loadUi("primeira_tela.ui")

        self.primeira_tela.pushButton.clicked.connect(self.plot_1)

        self.primeira_tela.pushButton_2.clicked.connect(self.plot_2)

        self.primeira_tela.pushButton_3.clicked.connect(self.plot_3)

        self.primeira_tela.pushButton_4.clicked.connect(self.textual)


        self.primeira_tela.show()

        self.app.exec()
execut()
