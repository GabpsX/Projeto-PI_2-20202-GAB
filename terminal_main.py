############################################################
## Dados da Equipe                                        ##
############################################################

############################################################
## Aluno: Gabriel Pereira Silva                           ##
## COMP0334 - PROGRAMAÇÃO IMPERATIVA (2020.2 - TURMA-T11) ##
############################################################

############################################################
# Arquivos com bibliotecas definidas pelo(a) programador(a)#
############################################################
#importando os aquivos contendo o codigo para gerar os #graficos e a resposta textual
from pathlib import Path


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
if arquivo.is_file() or arquivo1.is_file() or arquivo2.is_file() or arquivo3.is_file():
  print("Verificando arquivos!")
else:
  print("Tratando Dados!")
  tratardados_glinha.tratar_dados_linha()
  tratardados_gbarra.tratar_dados_barra()
  tratardados_gboxplot.tratar_dados_box_plot()
  tratardados_resposta_textual.tratar_dados_resposta()



def apresentar_tudo():
  import graph_linha
  import graph_barra
  import graph_boxplot
  import gerar_resposta_textual



  ############################################################
  # Interface de interação com o usuário                     #
  ############################################################

  print('Seja Bem-vindo! Voçê tem 3 opções de Gráficos e uma resposta textual: ')
  print('1: Gráfico de linha')
  print('2: Gráfico de barras')
  print('3: Gráfico box plot')
  print('4: Resposta Textual')
  entrada = int(input('Digite 1, 2, 3 ou 4: '))
  ############################################################
  while True:  # laço para escolher opção 1, 2, 3 ou 4.

      if entrada == 1:
          graph_linha.desempenho_pais()
          break

      elif entrada == 2:
          graph_barra.apresentar_graficobarra()
          break
      elif entrada == 3:
          graph_boxplot.apresentar_graficoboxplot()
          break
      elif entrada == 4:
          gerar_resposta_textual.reposta_text()
          break

      else:
          entrada = int(input('Numero Invalido!, Digite 1, 2, 3 ou 4: '))
          continue
apresentar_tudo()
        