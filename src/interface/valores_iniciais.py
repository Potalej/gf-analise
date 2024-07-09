"""
Funcoes para lidar com valores iniciais

Objetivos:
  Funcoes para lidar com a entrada e saida de arquivos de valores
  iniciais.

Modificado:
  09 de julho de 2024

Autoria:
  oap
"""

__version__ = "20240709"
__author__  = "oap"

from src.arquivos.ler import ler_valores_iniciais
from src.visualizacao import visual_matplotlib, visual_pygame
from src.interface import auxiliares 
from config.const import PARAMS, MOTORES

def valores_iniciais (argumentos:list)->None:
  # Le o arquivo
  diretorio = argumentos[-1]
  infos = ler_valores_iniciais(diretorio)

  # Verifica se quer exibir os pontos iniciais em 2d
  if auxiliares.verifica_argumentos(argumentos, PARAMS["E2D"]):

    # Captura os argumentos da exibicao
    indice = auxiliares.captura_primeiro_indice(argumentos, PARAMS["E2D"])
    eixo_x, eixo_y = auxiliares.captura_eixos(argumentos, indice)

    # Captura o motor escolhido para visualizacao
    motor = auxiliares.escolha_motor(argumentos, "vi_2d")

    # Roda
    motor(infos["corpos"], int(eixo_x), int(eixo_y))

  # Verifica se quer exibir os pontos iniciais em 3d
  elif auxiliares.verifica_argumentos(argumentos, PARAMS["E3D"]):
    
    # Captura o motor escolhido para visualizacao
    motor = auxiliares.escolha_motor(argumentos, "vi_2d")
    
    # Roda
    motor(infos["corpos"])

  return