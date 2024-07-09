"""
TESTE: Dados de simulacao em 3D

Objetivos:
  Testar a visualizacao de dados de simulacao em 3D.

Modificado:
  09 de julho de 2024

Autoria:
  oap
"""

__version__ = "20240709"
__author__  = "oap"

import sys
from src.arquivos.ler import ler_dados_simulacao
from src.visualizacao import visual_matplotlib

def teste ():
  # Arquivo utilizado
  arquivo = "./testes/data/dados_simulacao.csv"

  ##################
  # > leitura
  ##################
  try:
    infos = ler_dados_simulacao(arquivo)
  except:
    sys.exit("Erro na leitura do arquivo!")

  ##################
  # > matplotlib
  ##################
  try:
    visual_matplotlib.exibir_trajetorias_3d(infos["corpos"])
  except:
    sys.exit("Erro no plot via matplotlib!")