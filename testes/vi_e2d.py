"""
TESTE: Valores iniciais em 2D

Objetivos:
  Testar a visualizacao de valores iniciais em 2D.

Modificado:
  09 de julho de 2024

Autoria:
  oap
"""

__version__ = "20240709"
__author__  = "oap"

import sys
from src.arquivos.ler import ler_valores_iniciais
from src.visualizacao import visual_matplotlib, visual_pygame

def teste ():
  # Arquivo utilizado
  arquivo = "./testes/data/valor_inicial.txt"

  ##################
  # > leitura
  ##################
  try:
    infos = ler_valores_iniciais(arquivo)
  except:
    sys.exit("Erro na leitura do arquivo!")

  ##################
  # > matplotlib
  ##################
  try:
    eixo_x, eixo_y = 0, 1
    visual_matplotlib.exibir_pontos_2d(infos["corpos"], eixo_x, eixo_y)
  except:
    sys.exit("Erro no plot via matplotlib!")

  ##################
  # > pygame
  ##################
  try:
    eixo_x, eixo_y = 0, 1
    visual_pygame.exibir_trajetorias_2d(infos["corpos"], eixo_x, eixo_y)
  except:
    sys.exit("Erro no plot via pygame!")